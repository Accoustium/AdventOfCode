from typing import *


CaveAlias = "Cave"
MapAlias = "Map"


class Cave:
    def __init__(self, name: AnyStr):
        self.name = name
        self.big = name.isupper()
        self.traveled = False
        self.connection = set()

    def __repr__(self) -> AnyStr:
        return f"Tunnel({self.name}, big?={self.big})"

    def __hash__(self) -> AnyStr:
        return hash(self.name)

    def __eq__(self, other):
        if (
            self.name == other.name and
            self.big == other.big and
            self.traveled == other.traveled
        ):
            return True
        return False

    def add_connection(self, tunnel: CaveAlias):
        self.connection.add(tunnel)

    def find_tunnel(self, tunnel_name: AnyStr) -> CaveAlias:
        return_tun = None
        if self.name == tunnel_name:
            return_tun = self
        else:
            for tun in self.connection:
                if tun.name != tunnel_name:
                    return_tun = tun.find_tunnel(tunnel_name)
                else:
                    return_tun = tun

        return return_tun


class Map:
    def __init__(self):
        self.data = {}
        self.start: Optional[Cave] = None

    def add_route(self, start: AnyStr, stop: AnyStr):
        _start, _stop = Cave(start), Cave(stop)
        if _start not in self.data.keys():
            self.data[_start] = _start
        if _stop not in self.data.keys():
            self.data[_stop] = _stop
        self.data[_start].add_connection(_stop)
        self.data[_stop].add_connection(_start)

    def find_tunnel(self, tunnel_name: AnyStr) -> Cave:
        return self.start.find_tunnel(tunnel_name)

    def find_paths(self):
        ...


def load_map() -> Map:
    m = Map()
    with open('test_1.txt', "r") as file:
        for line in file:
            m.add_route(*line.strip().split("-"))

    m.start = m.data[Cave("start")]

    return m
