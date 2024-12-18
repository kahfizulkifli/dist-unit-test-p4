/* -*- P4_16 -*- */
#include <core.p4>
#include <v1model.p4>

const bit<16> TYPE_IPV4 = 0x800;
const bit<16> TYPE_UNIT_TEST = 0x812;

#define MAX_UNIT_TESTS 100


/*************************************************************************
*********************** H E A D E R S  ***********************************
*************************************************************************/

typedef bit<9>  egressSpec_t;
typedef bit<48> macAddr_t;
typedef bit<32> ip4Addr_t;

header ethernet_t {
    macAddr_t dstAddr;
    macAddr_t srcAddr;
    bit<16>   etherType;
}

// Header for storing unit test id
header unit_test_t {
    bit<16> testId;
    bit<8> testStatus;
}

struct metadata {
    bit<8> counter;
}

struct headers {
    ethernet_t   ethernet;
    unit_test_t  unit_test;
}

/*************************************************************************
*********************** P A R S E R  ***********************************
*************************************************************************/
typedef bit<16> counter_t;
typedef bit<8> test_status_t;
register<counter_t>(1) counter_test_id;
register<test_status_t>(MAX_UNIT_TESTS) unit_test_state;

parser MyParser(packet_in packet,
                out headers hdr,
                inout metadata meta,
                inout standard_metadata_t standard_metadata) {

    state start {
        transition parse_ethernet;
    }

    state parse_ethernet {
        packet.extract(hdr.ethernet);
        transition select(hdr.ethernet.etherType) {
            TYPE_UNIT_TEST: parse_unit_test;
            default : accept;
        }
    }

    state parse_unit_test {
        packet.extract(hdr.unit_test);
        transition accept;
    }
}


/*************************************************************************
************   C H E C K S U M    V E R I F I C A T I O N   *************
*************************************************************************/

control MyVerifyChecksum(inout headers hdr, inout metadata meta) {
    apply {  }
}


/*************************************************************************
**************  I N G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyIngress(inout headers hdr,
                  inout metadata meta,
                  inout standard_metadata_t standard_metadata) {

    counter_t tmp_count;

    action drop() {
        mark_to_drop(standard_metadata);
    }

    action get_unit_test() {
        bit<48> tmp;
        counter_test_id.read(tmp_count, 0x00);
        tmp_count = tmp_count + 1;
        log_msg("Ingress incremented counter_test_id[p] {}",
            {tmp_count});
        counter_test_id.write(0x00, tmp_count);
        unit_test_state.write((bit<32>)hdr.unit_test.testId, hdr.unit_test.testStatus);

        if (tmp_count > MAX_UNIT_TESTS) {
            hdr.unit_test.testId = 999;
        } else {
            hdr.unit_test.testId = tmp_count - 1;
        }
        tmp = hdr.ethernet.dstAddr;
        hdr.ethernet.dstAddr = hdr.ethernet.srcAddr;
        hdr.ethernet.srcAddr = tmp;

        standard_metadata.egress_spec = standard_metadata.ingress_port;
    }

    apply {
        if (hdr.unit_test.isValid())
            get_unit_test();
    }
}

/*************************************************************************
****************  E G R E S S   P R O C E S S I N G   *******************
*************************************************************************/

control MyEgress(inout headers hdr,
                 inout metadata meta,
                 inout standard_metadata_t standard_metadata) {

    apply {  }
}

/*************************************************************************
*************   C H E C K S U M    C O M P U T A T I O N   **************
*************************************************************************/

control MyComputeChecksum(inout headers hdr, inout metadata meta) {
     apply {  }
}


/*************************************************************************
***********************  D E P A R S E R  *******************************
*************************************************************************/

control MyDeparser(packet_out packet, in headers hdr) {
    apply {
        packet.emit(hdr.ethernet);
        packet.emit(hdr.unit_test);
    }
}

/*************************************************************************
***********************  S W I T C H  *******************************
*************************************************************************/

V1Switch(
MyParser(),
MyVerifyChecksum(),
MyIngress(),
MyEgress(),
MyComputeChecksum(),
MyDeparser()
) main;
