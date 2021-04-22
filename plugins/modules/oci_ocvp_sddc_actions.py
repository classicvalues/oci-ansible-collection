#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_ocvp_sddc_actions
short_description: Perform actions on a Sddc resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Sddc resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an SDDC into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9"
author: Oracle (@oracle)
options:
    sddc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SDDC.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to move
              the SDDC to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Sddc.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on sddc
  oci_ocvp_sddc_actions:
    sddc_id: "ocid1.sddc.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
sddc:
    description:
        - Details of the Sddc resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the SDDC.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compute_availability_domain:
            description:
                - The availability domain the ESXi hosts are running in.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: string
            sample: Uocm:PHX-AD-1
        display_name:
            description:
                - A descriptive name for the SDDC. It must be unique, start with a letter, and contain only letters, digits,
                  whitespaces, dashes and underscores.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        instance_display_name_prefix:
            description:
                - A prefix used in the name of each ESXi host and Compute instance in the SDDC.
                  If this isn't set, the SDDC's `displayName` is used as the prefix.
                - For example, if the value is `MySDDC`, the ESXi hosts are named `MySDDC-1`,
                  `MySDDC-2`, and so on.
            returned: on success
            type: string
            sample: instance_display_name_prefix_example
        vmware_software_version:
            description:
                - In general, this is a specific version of bundled VMware software supported by
                  Oracle Cloud VMware Solution (see
                  L(ListSupportedVmwareSoftwareVersions,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/vmware/20200501/SupportedVmwareSoftwareVersionSummary/ListSupportedVmwareSoftwareVersions)).
                - "This attribute is not guaranteed to reflect the version of
                  software currently installed on the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the version of software that the Oracle
                  Cloud VMware Solution will install on any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you upgrade the existing ESXi hosts in the SDDC to use a newer
                  version of bundled VMware software supported by the Oracle Cloud VMware Solution, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `vmwareSoftwareVersion` with that new version.
            returned: on success
            type: string
            sample: vmware_software_version_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that
                  contains the SDDC.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        esxi_hosts_count:
            description:
                - The number of ESXi hosts in the SDDC.
            returned: on success
            type: int
            sample: 56
        initial_sku:
            description:
                - Billing option selected during SDDC creation
                  L(ListSupportedSkus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/SupportedSkuSummary/ListSupportedSkus).
            returned: on success
            type: string
            sample: HOUR
        vcenter_fqdn:
            description:
                - The FQDN for vCenter.
                - "Example: `vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com`"
            returned: on success
            type: string
            sample: vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com
        nsx_manager_fqdn:
            description:
                - The FQDN for NSX Manager.
                - "Example: `nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`"
            returned: on success
            type: string
            sample: nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com
        vcenter_private_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PrivateIp` object that is
                  the virtual IP (VIP) for vCenter. For information about `PrivateIp` objects, see the
                  Core Services API.
            returned: on success
            type: string
            sample: "ocid1.vcenterprivateip.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_manager_private_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PrivateIp` object that is
                  the virtual IP (VIP) for NSX Manager. For information about `PrivateIp` objects, see the
                  Core Services API.
            returned: on success
            type: string
            sample: "ocid1.nsxmanagerprivateip.oc1..xxxxxxEXAMPLExxxxxx"
        vcenter_initial_password:
            description:
                - The SDDC includes an administrator username and initial password for vCenter. Make sure
                  to change this initial vCenter password to a different value.
            returned: on success
            type: string
            sample: vcenter_initial_password_example
        nsx_manager_initial_password:
            description:
                - The SDDC includes an administrator username and initial password for NSX Manager. Make sure
                  to change this initial NSX Manager password to a different value.
            returned: on success
            type: string
            sample: nsx_manager_initial_password_example
        vcenter_username:
            description:
                - The SDDC includes an administrator username and initial password for vCenter. You can
                  change this initial username to a different value in vCenter.
            returned: on success
            type: string
            sample: vcenter_username_example
        nsx_manager_username:
            description:
                - The SDDC includes an administrator username and initial password for NSX Manager. You
                  can change this initial username to a different value in NSX Manager.
            returned: on success
            type: string
            sample: nsx_manager_username_example
        ssh_authorized_keys:
            description:
                - One or more public SSH keys to be included in the `~/.ssh/authorized_keys` file for
                  the default user on each ESXi host. Use a newline character to separate multiple keys.
                  The SSH keys must be in the format required for the `authorized_keys` file.
                - "This attribute is not guaranteed to reflect the public SSH keys
                  currently installed on the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the public SSH keys that Oracle
                  Cloud VMware Solution will install on any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you upgrade the existing ESXi hosts in the SDDC to use different
                  SSH keys, you should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update
                  the SDDC's `sshAuthorizedKeys` with the new public keys.
            returned: on success
            type: string
            sample: ssh_authorized_keys_example
        workload_network_cidr:
            description:
                - The CIDR block for the IP addresses that VMware VMs in the SDDC use to run application
                  workloads.
            returned: on success
            type: string
            sample: workload_network_cidr_example
        nsx_overlay_segment_name:
            description:
                - The VMware NSX overlay workload segment to host your application. Connect to workload
                  portgroup in vCenter to access this overlay segment.
            returned: on success
            type: string
            sample: nsx_overlay_segment_name_example
        nsx_edge_uplink_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PrivateIp` object that is
                  the virtual IP (VIP) for the NSX Edge Uplink. Use this OCID as the route target for
                  route table rules when setting up connectivity between the SDDC and other networks.
                  For information about `PrivateIp` objects, see the Core Services API.
            returned: on success
            type: string
            sample: "ocid1.nsxedgeuplinkip.oc1..xxxxxxEXAMPLExxxxxx"
        provisioning_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the management subnet used
                  to provision the SDDC.
            returned: on success
            type: string
            sample: "ocid1.provisioningsubnet.oc1..xxxxxxEXAMPLExxxxxx"
        vsphere_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the vSphere component of the VMware environment.
                - "This attribute is not guaranteed to reflect the vSphere VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the vSphere VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the vSphere component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `vsphereVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: "ocid1.vspherevlan.oc1..xxxxxxEXAMPLExxxxxx"
        vmotion_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the vMotion component of the VMware environment.
                - "This attribute is not guaranteed to reflect the vMotion VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the vMotion VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the vMotion component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `vmotionVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: "ocid1.vmotionvlan.oc1..xxxxxxEXAMPLExxxxxx"
        vsan_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the vSAN component of the VMware environment.
                - "This attribute is not guaranteed to reflect the vSAN VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the vSAN VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the vSAN component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `vsanVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: "ocid1.vsanvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_v_tep_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the NSX VTEP component of the VMware environment.
                - "This attribute is not guaranteed to reflect the NSX VTEP VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the NSX VTEP VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the NSX VTEP component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `nsxVTepVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: "ocid1.nsxvtepvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_v_tep_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the NSX Edge VTEP component of the VMware environment.
                - "This attribute is not guaranteed to reflect the NSX Edge VTEP VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the NSX Edge VTEP VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the NSX Edge VTEP component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `nsxEdgeVTepVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: "ocid1.nsxedgevtepvlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_uplink1_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the NSX Edge Uplink 1 component of the VMware environment.
                - "This attribute is not guaranteed to reflect the NSX Edge Uplink 1 VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the NSX Edge Uplink 1 VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the NSX Edge Uplink 1 component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `nsxEdgeUplink1VlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: "ocid1.nsxedgeuplink1vlan.oc1..xxxxxxEXAMPLExxxxxx"
        nsx_edge_uplink2_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the NSX Edge Uplink 2 component of the VMware environment.
                - "This attribute is not guaranteed to reflect the NSX Edge Uplink 2 VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the NSX Edge Uplink 2 VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the NSX Edge Uplink 2 component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `nsxEdgeUplink2VlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: "ocid1.nsxedgeuplink2vlan.oc1..xxxxxxEXAMPLExxxxxx"
        replication_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the vSphere Replication component of the VMware environment.
            returned: on success
            type: string
            sample: "ocid1.replicationvlan.oc1..xxxxxxEXAMPLExxxxxx"
        provisioning_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the Provisioning component of the VMware environment.
            returned: on success
            type: string
            sample: "ocid1.provisioningvlan.oc1..xxxxxxEXAMPLExxxxxx"
        hcx_private_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the `PrivateIp` object that is
                  the virtual IP (VIP) for HCX Manager. For information about `PrivateIp` objects, see the
                  Core Services API.
            returned: on success
            type: string
            sample: "ocid1.hcxprivateip.oc1..xxxxxxEXAMPLExxxxxx"
        hcx_fqdn:
            description:
                - The FQDN for HCX Manager.
                - "Example: `hcx-my-sddc.sddc.us-phoenix-1.oraclecloud.com`"
            returned: on success
            type: string
            sample: hcx-my-sddc.sddc.us-phoenix-1.oraclecloud.com
        hcx_initial_password:
            description:
                - The SDDC includes an administrator username and initial password for HCX Manager. Make sure
                  to change this initial HCX Manager password to a different value.
            returned: on success
            type: string
            sample: hcx_initial_password_example
        hcx_vlan_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VLAN used by the SDDC
                  for the HCX component of the VMware environment.
                - "This attribute is not guaranteed to reflect the HCX VLAN
                  currently used by the ESXi hosts in the SDDC. The purpose
                  of this attribute is to show the HCX VLAN that the Oracle
                  Cloud VMware Solution will use for any new ESXi hosts that you *add to this
                  SDDC in the future* with L(CreateEsxiHost,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/EsxiHost/CreateEsxiHost)."
                - Therefore, if you change the existing ESXi hosts in the SDDC to use a different VLAN
                  for the HCX component of the VMware environment, you
                  should use L(UpdateSddc,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/vmware/20200501/Sddc/UpdateSddc) to update the SDDC's
                  `hcxVlanId` with that new VLAN's OCID.
            returned: on success
            type: string
            sample: "ocid1.hcxvlan.oc1..xxxxxxEXAMPLExxxxxx"
        is_hcx_enabled:
            description:
                - Indicates whether HCX is enabled for this SDDC.
            returned: on success
            type: bool
            sample: true
        hcx_on_prem_key:
            description:
                - The activation key to use on the on-premises HCX Enterprise appliance you site pair with HCX Manager in your VMware Solution.
                  Your implementation might need more than one activation key. To obtain additional keys, contact Oracle Support.
            returned: on success
            type: string
            sample: hcx_on_prem_key_example
        time_created:
            description:
                - The date and time the SDDC was created, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        time_updated:
            description:
                - The date and time the SDDC was updated, in the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the SDDC.
            returned: on success
            type: string
            sample: CREATING
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_availability_domain": "Uocm:PHX-AD-1",
        "display_name": "display_name_example",
        "instance_display_name_prefix": "instance_display_name_prefix_example",
        "vmware_software_version": "vmware_software_version_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "esxi_hosts_count": 56,
        "initial_sku": "HOUR",
        "vcenter_fqdn": "vcenter-my-sddc.sddc.us-phoenix-1.oraclecloud.com",
        "nsx_manager_fqdn": "nsx-my-sddc.sddc.us-phoenix-1.oraclecloud.com",
        "vcenter_private_ip_id": "ocid1.vcenterprivateip.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_manager_private_ip_id": "ocid1.nsxmanagerprivateip.oc1..xxxxxxEXAMPLExxxxxx",
        "vcenter_initial_password": "vcenter_initial_password_example",
        "nsx_manager_initial_password": "nsx_manager_initial_password_example",
        "vcenter_username": "vcenter_username_example",
        "nsx_manager_username": "nsx_manager_username_example",
        "ssh_authorized_keys": "ssh_authorized_keys_example",
        "workload_network_cidr": "workload_network_cidr_example",
        "nsx_overlay_segment_name": "nsx_overlay_segment_name_example",
        "nsx_edge_uplink_ip_id": "ocid1.nsxedgeuplinkip.oc1..xxxxxxEXAMPLExxxxxx",
        "provisioning_subnet_id": "ocid1.provisioningsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "vsphere_vlan_id": "ocid1.vspherevlan.oc1..xxxxxxEXAMPLExxxxxx",
        "vmotion_vlan_id": "ocid1.vmotionvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "vsan_vlan_id": "ocid1.vsanvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_v_tep_vlan_id": "ocid1.nsxvtepvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_edge_v_tep_vlan_id": "ocid1.nsxedgevtepvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_edge_uplink1_vlan_id": "ocid1.nsxedgeuplink1vlan.oc1..xxxxxxEXAMPLExxxxxx",
        "nsx_edge_uplink2_vlan_id": "ocid1.nsxedgeuplink2vlan.oc1..xxxxxxEXAMPLExxxxxx",
        "replication_vlan_id": "ocid1.replicationvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "provisioning_vlan_id": "ocid1.provisioningvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "hcx_private_ip_id": "ocid1.hcxprivateip.oc1..xxxxxxEXAMPLExxxxxx",
        "hcx_fqdn": "hcx-my-sddc.sddc.us-phoenix-1.oraclecloud.com",
        "hcx_initial_password": "hcx_initial_password_example",
        "hcx_vlan_id": "ocid1.hcxvlan.oc1..xxxxxxEXAMPLExxxxxx",
        "is_hcx_enabled": true,
        "hcx_on_prem_key": "hcx_on_prem_key_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.ocvp import SddcClient
    from oci.ocvp.models import ChangeSddcCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SddcActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "sddc_id"

    def get_module_resource_id(self):
        return self.module.params.get("sddc_id")

    def get_get_fn(self):
        return self.client.get_sddc

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sddc, sddc_id=self.module.params.get("sddc_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSddcCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_sddc_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                sddc_id=self.module.params.get("sddc_id"),
                change_sddc_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


SddcActionsHelperCustom = get_custom_class("SddcActionsHelperCustom")


class ResourceHelper(SddcActionsHelperCustom, SddcActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            sddc_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="sddc",
        service_client_class=SddcClient,
        namespace="ocvp",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
