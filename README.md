# Computer-Network-Course-Design
# 基于 NETCONF 的小型企业网 SDN 自动化部署

## 项目简介
本项目为计算机网络课程设计作品。旨在通过 Python 编程与 NETCONF 协议，实现对 H3C 网络设备的自动化配置与管理。项目实现了 VLAN 划分、IP 地址配置、静态路由下发、DHCP 服务部署及 NAT 策略配置的全流程自动化。

## 环境要求
*   **操作系统**: Windows 10/11
*   **编程语言**: Python 3.9+
*   **依赖库**: `ncclient`
*   **仿真软件**: H3C Cloud Lab (HCL) v5.9.0
  
### 文件作用简述

*   **`netconf_utils.py` (核心工具模块)**
    *   **作用**：封装了 `ncclient` 库的底层操作。它负责建立与设备的 SSH 连接、发送 XML 配置报文、处理设备响应以及发送 `<save/>` 命令保存配置。
    *   **注意**：这是一个库文件，**不需要直接运行**，其他脚本会调用它。

*   **`get_table.py` (侦测脚本)**
    *   **作用**：用于连接设备并获取接口列表信息。
    *   **目的**：帮助开发者查询接口名称（如 GE0/0）对应的内部索引号 **`IfIndex`**，这是编写后续配置脚本的基础。

*   **`s1_vlan_trunk.py` (步骤一：二层网络配置)**
    *   **作用**：在核心交换机和接入交换机上批量创建 VLAN 10 和 VLAN 20，并将 Access 端口划入对应 VLAN，同时配置交换机互联接口为 Trunk 模式。

*   **`s2_ip_address.py` (步骤二：三层互联配置)**
    *   **作用**：配置路由器 (R1) 和核心交换机 (Core) 之间物理互联接口的 IP 地址。

*   **`s3_static_route.py` (步骤三：路由策略配置)**
    *   **作用**：下发静态路由。配置 Core 指向 R1 的默认路由，以及 R1 指向内网业务网段的汇总路由。

*   **`s4_dhcp_nat.py` (步骤四：网络服务配置)**
    *   **作用**：在 Core 上配置 DHCP 地址池；在 R1 上配置 NAT Outbound 策略（绑定 ACL 与外网接口）。
      
## 快速开始

### 1. 安装依赖
请确保已安装 Python 环境，并在终端执行以下命令安装核心库：
```bash
pip install ncclient
```

### 2. 基础环境准备 (Underlay)
在运行 Python 脚本前，需在 HCL 模拟器中完成以下基础配置：
1.  **搭建拓扑**：连接 R1, Core, Access, MGMT 交换机及 Cloud。
2.  **配置管理 IP**：
    *   R1 (M-GE0/0): 15.79.100.1
    *   Core (M-GE0/0): 15.79.100.2
    *   Access (M-GE0/0): 15.79.100.3
3.  **开启服务**：在所有设备上开启 SSH 及 NETCONF 服务，并创建管理员账号 `abcadmin`。

### 3. 自动化部署流程 (请严格按顺序执行)

本项目采用模块化设计，请按照以下顺序运行脚本：

#### 第一步：部署二层网络
运行脚本：`s1_vlan_trunk.py`
> **功能**：创建 VLAN 10/20，配置 Access/Trunk 接口。

#### 第二步：部署三层互联 IP
运行脚本：`s2_ip_address.py`
> **功能**：配置 R1 与 Core 之间的物理接口 IP。

#### 第三步：【人工干预】配置 VLAN 网关
由于 VLAN 虚接口索引动态生成，需在 **Core 交换机** 命令行手动补充：
```h3c
interface Vlan-interface 10
 ip address 32.32.10.254 24
interface Vlan-interface 20
 ip address 32.32.20.254 24
```

#### 第四步：部署路由策略
运行脚本：`s3_static_route.py`
> **功能**：下发全网静态路由，打通路由表。

#### 第五步：部署 DHCP 与 NAT
运行脚本：`s4_dhcp_nat.py`
> **功能**：配置 DHCP 地址池及 NAT 规则。
> **注意**：运行后需在 **R1 路由器** 命令行手动补充 ACL 规则：
> `acl basic 2000` -> `rule permit source 32.32.0.0 0.0.255.255`

## 验证方法
1.  **DHCP 验证**：使用模拟 PC (Host01) 获取 IP，检查是否获得 `32.32.10.x` 网段地址。
2.  **连通性验证**：Host01 应能 Ping 通 Host03 (跨 VLAN) 及 Internet 模拟节点 (跨 NAT)。
3.  **NAT 验证**：在 R1 上执行 `display nat session verbose`，查看地址转换表项。

## 文件结构说明
*   `netconf_utils.py`: 通用工具类，封装 NETCONF 连接与 XML 发送逻辑。
*   `get_table.py`: 辅助脚本，用于获取设备接口 IfIndex。
*   `s1_` ~ `s4_`: 业务逻辑脚本，对应不同的网络配置阶段。

## 作者
*   Andy.Xu.Prime
*   日期：2026-01-14
