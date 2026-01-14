from netconf_utils import send_netconf_config

# Core
CORE_XML = """
<config>
    <top xmlns="http://www.h3c.com/netconf/config:1.0">
        <VLAN><VLANs>
            <VLANID><ID>10</ID><Name>vlan10</Name></VLANID>
            <VLANID><ID>20</ID><Name>vlan20</Name></VLANID>
        </VLANs></VLAN>
        <Ifmgr><Interfaces><Interface>
            <IfIndex>2</IfIndex>
            <LinkType>2</LinkType> <!-- 2=Trunk -->
        </Interface></Interfaces></Ifmgr>
        <VLAN><TrunkInterfaces><Interface>
            <IfIndex>2</IfIndex>
            <PermitVlanList>10,20</PermitVlanList>
        </Interface></TrunkInterfaces></VLAN>
    </top>
</config>
"""

# Access（Vlan划分）
ACCESS_XML = """
<config>
    <top xmlns="http://www.h3c.com/netconf/config:1.0">
        <VLAN><VLANs>
            <VLANID>
                <ID>10</ID>
                <AccessPortList>2-3</AccessPortList> <!-- Host1, Host2 -->
            </VLANID>
            <VLANID>
                <ID>20</ID>
                <AccessPortList>4-5</AccessPortList> <!-- Host3, Host4 -->
            </VLANID>
        </VLANs></VLAN>
        <Ifmgr><Interfaces><Interface>
            <IfIndex>49</IfIndex> <!-- Access上联Core的接口 -->
            <LinkType>2</LinkType>
        </Interface></Interfaces></Ifmgr>
        <VLAN><TrunkInterfaces><Interface>
            <IfIndex>49</IfIndex>
            <PermitVlanList>10,20</PermitVlanList>
        </Interface></TrunkInterfaces></VLAN>
    </top>
</config>
"""

send_netconf_config("15.79.100.2", CORE_XML, "核心交换机 VLAN/Trunk 配置")
send_netconf_config("15.79.100.3", ACCESS_XML, "接入交换机 VLAN/Access/Trunk 配置")