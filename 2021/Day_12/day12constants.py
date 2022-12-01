from typing import *


TunnelAlias = "Tunnel"
MapAlias = "Map"


class Tunnel:
    def __init__(self, name: AnyStr):
        self.name = name
        self.big = name.isupper()
        self.traveled = False
        self.connection = list()

    def __repr__(self) -> AnyStr:
        return f"Tunnel({self.name}, big?={self.big})"

    def __hash__(self) -> AnyStr:
        return self.name

    def add_connection(self, tunnel: TunnelAlias):
        self.connection.append(tunnel)

    def find_tunnel(self, tunnel_name: AnyStr) -> TunnelAlias:
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
        self.start: Optional[Tunnel] = None

    def add_route(self, start: AnyStr, stop: AnyStr):
        if start not in self.data.keys():
            self.data[start] = list()
        if stop not in self.data.keys():
            self.data[stop] = list()
        self.data[start].append(stop)

    def find_tunnel(self, tunnel_name: AnyStr) -> Tunnel:
        return self.start.find_tunnel(tunnel_name)

    def find_paths(self):
        ...


def load_map() -> Map:
    m = Map()
    with open('test_1.txt', "r") as file:
        for line in file:
            m.add_route(*line.strip().split("-"))

    m.start = Tunnel('start')

    return m
