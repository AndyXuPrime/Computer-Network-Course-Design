from netconf_utils import send_netconf_config

#R_1579 路由配置
# 目的网段：32.32.0.0/16,下一跳：Core:15.79.0.2
R1_ROUTE_XML = """
<config>
    <top xmlns="http://www.h3c.com/netconf/config:1.0">
        <StaticRoute>
            <Ipv4StaticRouteConfigurations>
                <RouteEntry>
                    <Ipv4Address>32.32.0.0</Ipv4Address>
                    <Ipv4PrefixLength>16</Ipv4PrefixLength>
                    <NexthopIpv4Address>15.79.0.2</NexthopIpv4Address>

                    <DestVrfIndex>0</DestVrfIndex>
                    <DestTopologyIndex>0</DestTopologyIndex>
                    <NexthopVrfIndex>0</NexthopVrfIndex>
                    <IfIndex>0</IfIndex> <!-- 0:让设备自动查找出接口 -->

                </RouteEntry>
            </Ipv4StaticRouteConfigurations>
        </StaticRoute>
    </top>
</config>
"""

# Core 路由配置
# 下一跳：R_1579:15.79.0.1
CORE_ROUTE_XML = """
<config>
    <top xmlns="http://www.h3c.com/netconf/config:1.0">
        <StaticRoute>
            <Ipv4StaticRouteConfigurations>
                <RouteEntry>
                    <Ipv4Address>0.0.0.0</Ipv4Address>
                    <Ipv4PrefixLength>0</Ipv4PrefixLength>
                    <NexthopIpv4Address>15.79.0.1</NexthopIpv4Address>

                    <DestVrfIndex>0</DestVrfIndex>
                    <DestTopologyIndex>0</DestTopologyIndex>
                    <NexthopVrfIndex>0</NexthopVrfIndex>
                    <IfIndex>0</IfIndex>

                </RouteEntry>
            </Ipv4StaticRouteConfigurations>
        </StaticRoute>
    </top>
</config>
"""

send_netconf_config("15.79.100.1", R1_ROUTE_XML, "R1 回程路由配置")
send_netconf_config("15.79.100.2", CORE_ROUTE_XML, "Core 默认路由配置")