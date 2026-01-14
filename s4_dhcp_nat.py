from netconf_utils import send_netconf_config

#Core DHCP配置
DHCP_XML = """
<config>
    <top xmlns="http://www.h3c.com/netconf/config:1.0">
        <DHCP>
            <DHCPConfig>
                <DHCPEnable>true</DHCPEnable>
            </DHCPConfig>
            <DHCPServerIpPool>
                <IpPool>
                    <PoolIndex>1</PoolIndex><PoolName>vlan10_pool</PoolName>
                    <NetworkIpv4Address>32.32.10.0</NetworkIpv4Address>
                    <NetworkIpv4Mask>255.255.255.0</NetworkIpv4Mask>
                    <GatewayIpv4Address>32.32.10.254</GatewayIpv4Address>
                </IpPool>
                <IpPool>
                    <PoolIndex>2</PoolIndex><PoolName>vlan20_pool</PoolName>
                    <NetworkIpv4Address>32.32.20.0</NetworkIpv4Address>
                    <NetworkIpv4Mask>255.255.255.0</NetworkIpv4Mask>
                    <GatewayIpv4Address>32.32.20.254</GatewayIpv4Address>
                </IpPool>
            </DHCPServerIpPool>
        </DHCP>
    </top>
</config>
"""

#R_1579 NAT 配置
NAT_XML = """
<config>
    <top xmlns="http://www.h3c.com/netconf/config:1.0">
        <NAT>
            <OutboundDynamicRules>
                <Interface>
                    <IfIndex>2</IfIndex> <!-- R1579的外网口 IfIndex -->
                    <ACLNumber>2000</ACLNumber>
                    <NoPAT>false</NoPAT>
                </Interface>
            </OutboundDynamicRules>
        </NAT>
    </top>
</config>
"""

send_netconf_config("15.79.100.2", DHCP_XML, "Core DHCP 服务配置")
send_netconf_config("15.79.100.1", NAT_XML, "R1 NAT 接口配置")
