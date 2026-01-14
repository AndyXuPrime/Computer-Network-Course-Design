import xml.dom.minidom
from ncclient import manager

SWITCH_IP = "15.79.100.3"  #设备IP
SWITCH_PORT = 830
USERNAME = "abcadmin"
PASSWORD = "abc11223344"

# 获取接口列表及其索引
get_xml = """
<top xmlns="http://www.h3c.com/netconf/data:1.0">
  <Ifmgr>
    <Interfaces>
      <Interface>
        <IfIndex></IfIndex>
        <Name></Name>
      </Interface>
    </Interfaces>
  </Ifmgr>
</top>
"""


def get_interfaces(host, port, user, pwd):
    print(f"正在尝试连接设备 {host}...")
    try:
        with manager.connect(
                host=host,
                port=port,
                username=user,
                password=pwd,
                hostkey_verify=False,
                device_params={"name": "h3c"},
                allow_agent=False,
                look_for_keys=False,
                timeout=30  # 增加超时时间防止网络波动
        ) as m:
            print("连接成功！正在获取接口信息...")
            response = m.get(('subtree', get_xml))
            xml_str = xml.dom.minidom.parseString(response.xml).toprettyxml(indent="  ")

            print("\n" + "=" * 50)
            print(f"设备 {host} 返回的接口信息如下：")
            print("=" * 50)
            print(xml_str)
            print("=" * 50)

            #结果保存
            filename = f"interfaces_{host}.xml"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(xml_str)
            print(f"结果已同步保存至文件: {filename}")

    except Exception as e:
        print(f"\n[错误] 无法连接或获取信息: {e}")
        print("请检查：1. IP是否能ping通 2. 设备是否开启 netconf ssh server enable 3. 账号密码是否正确")


if __name__ == '__main__':
    get_interfaces(SWITCH_IP, SWITCH_PORT, USERNAME, PASSWORD)