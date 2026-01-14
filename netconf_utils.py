from ncclient import manager
from ncclient.xml_ import to_ele
import xml.dom.minidom

def send_netconf_config(target_ip, config_xml, task_name="配置任务"):
    print(f"\n>>> 正在执行: {task_name} -> 目标设备: {target_ip}")
    try:
        with manager.connect(host=target_ip, port=830,
                             username="abcadmin", password="abc11223344",
                             hostkey_verify=False, device_params={'name': "h3c"},
                             allow_agent=False, look_for_keys=False) as m:

            # 发送配置
            response = m.edit_config(target="running", config=config_xml)

            # 打印结果
            if "<ok/>" in response.xml:
                print(f"成功！设备 {target_ip} 已接受配置。")
            else:
                print(f"警告：设备 {target_ip} 返回了非OK响应：")
                print(xml.dom.minidom.parseString(response.xml).toprettyxml())

            save_rpc = "<save/>"
            m.dispatch(to_ele(save_rpc))
            print("配置已保存到设备启动项。")

    except Exception as e:
        print(f"连接或配置设备 {target_ip} 失败: {e}")