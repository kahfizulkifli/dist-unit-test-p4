from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        # Add hosts and switches
        h1 = self.addHost( 'h1', ip="10.0.0.1/24", mac="08:00:00:00:01:11" )
        h2 = self.addHost( 'h2', ip="10.0.0.2/24", mac="08:00:00:00:02:22" )
        h3 = self.addHost( 'h3', ip="10.0.0.3/24", mac="08:00:00:00:03:33" )
        h4 = self.addHost( 'h4', ip="10.0.0.4/24", mac="08:00:00:00:04:44" )
        h5 = self.addHost( 'h5')

        # Add links
        self.addLink( h1, h5 )
        self.addLink( h2, h5 )
        self.addLink( h3, h5 )
        self.addLink( h4, h5 )


topos = { 'mytopo': ( lambda: MyTopo() ) }
