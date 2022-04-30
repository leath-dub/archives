.TL
Notes on Network measures
.LP
l = Length of a path, in meters

v = Signal propagation speed, in meters/sec

L = Average length of frame or packet, in bits

C = Transmission rate, in bits/sec



Propagation delay: We need l & v -> l/v

Transmission time: need L & C -> L/C

Throughput: Number of packets it can transmit per second, single nodes, whole network(sum of each nodes throughput)

Efficiency: current throughput/Max capacity

-----

Propagated packets/frames = propagation delay / transmission time

Total travel time = transmission time + [n intermediate nodes * m packets(at each node) * transmission time]

The pure transmission delay is how long the packet takes to get to receiver excluding queued packets it encounters at
each node, i.e.:

pure transmission delay = transmission time + [n nodes * transmission time]


The queuing delay is the time a packet must wait at a given node based on its position in the queue of other packets
i.e.:

node queuing delay = n packets in the queue * transmission time


Additionally the total queuing delay is -> n nodes * queuing delay, assuming queuing delay is the same at each node.
