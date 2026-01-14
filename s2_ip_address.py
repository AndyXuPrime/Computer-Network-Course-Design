from netconf_utils import send_netconf_config

#R_1579
R1_IP_XML = """
<config>
    <top xmlns="http://www.h3c.com/netconf/config:1.0">
        <IPV4ADDRESS><Ipv4Addresses><Ipv4Address>
            <IfIndex>1</IfIndex>
            <Ipv4Address>15.79.0.1</Ipv4Address>
            <Ipv4Mask>255.255.255.252</Ipv4Mask>
        </Ipv4Address></Ipv4Addresses></IPV4ADDRESS>
    </top>
</config>
"""

#Core
CORE_IP_XML = """
<config>
    <top xmlns="http://www.h3c.com/netconf/config:1.0">
        <IPV4ADDRESS><Ipv4Addresses>
            <Ipv4Address>
                <IfIndex>49</IfIndex>
                <Ipv4Address>15.79.0.2</Ipv4Address>
                <Ipv4Mask>255.255.255.252</Ipv4Mask>
            </Ipv4Address>
        </Ipv4Addresses></IPV4ADDRESS>
    </top>
</config>
"""

send_netconf_config("15.79.100.1", R1_IP_XML, "R1 物理接口 IP 配置")
send_netconf_config("15.79.100.2", CORE_IP_XML, "Core 物理接口 IP 配置")
