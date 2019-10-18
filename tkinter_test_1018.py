#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
tkinterで必要なもの
"""
import tkinter
from tkinter import ttk



class get_info():
    """
    APIによる情報取得
    """

    def __init__(self, host, api_secret_key):
        self.host = host
        self.header = {
                        "api-secret-key": api_secret_key,
                        "api-version": "v1"
                        }

        self.get_users_info()
        self.get_roles_info()
        self.get_api_keys_info()
    
    def get_users_info(self):

        users = [
                    {'ID': 1,
                    'UTCOffset': 'UTC+9.00',
                    'active': True,
                    'created': 1544610790133,
                    'description': '',
                    'emailAddress': '',
                    'external': False,
                    'fullName': '',
                    'lastPasswordChange': 1544610790133,
                    'lastSignIn': 1564479177803,
                    'locale': 'ja-JP',
                    'mfaType': 'none',
                    'mobileNumber': '',
                    'pagerNumber': '',
                    'passwordNeverExpires': False,
                    'phoneNumber': '',
                    'primaryContact': False,
                    'readOnly': False,
                    'receiveNotifications': False,
                    'reportPDFPasswordEnabled': False,
                    'roleID': 1,
                    'timeFormat': '24',
                    'timeZone': 'Asia/Tokyo',
                    'type': 'normal',
                    'unsuccessfulSignInAttempts': 0,
                    'username': 'MasterAdmin'},
                    {'ID': 4,
                    'UTCOffset': 'UTC+9.00',
                    'active': True,
                    'created': 1564479208537,
                    'description': '',
                    'emailAddress': '',
                    'external': False,
                    'fullName': '',
                    'lastPasswordChange': 1564479208537,
                    'locale': 'ja-JP',
                    'mfaType': 'none',
                    'mobileNumber': '',
                    'pagerNumber': '',
                    'passwordNeverExpires': False,
                    'phoneNumber': '',
                    'primaryContact': False,
                    'readOnly': False,
                    'receiveNotifications': False,
                    'reportPDFPasswordEnabled': False,
                    'roleID': 1,
                    'timeFormat': '24',
                    'timeZone': 'Asia/Tokyo',
                    'type': 'normal',
                    'unsuccessfulSignInAttempts': 0,
                    'username': 'test_user'},
                    {'ID': 5,
                    'UTCOffset': 'UTC+0.00',
                    'active': True,
                    'created': 1564479263677,
                    'description': '',
                    'emailAddress': '',
                    'external': False,
                    'fullName': '',
                    'lastPasswordChange': 1564479263677,
                    'locale': 'en-US',
                    'mfaType': 'none',
                    'mobileNumber': '',
                    'pagerNumber': '',
                    'passwordNeverExpires': False,
                    'phoneNumber': '',
                    'primaryContact': False,
                    'readOnly': False,
                    'receiveNotifications': False,
                    'reportPDFPasswordEnabled': False,
                    'roleID': 2,
                    'timeFormat': '24',
                    'timeZone': 'Etc/GMT',
                    'type': 'normal',
                    'unsuccessfulSignInAttempts': 0,
                    'username': 'test_user_1'}]
        self.users = users
        return self.users
    
    def get_roles_info(self):

        roles = [{'ID': 1,
                   'allComputers': True,
                   'allPolicies': True,
                   'allowUserInterface': True,
                   'allowWebService': True,
                   'canOnlyManipulateUsersWithEqualOrLesserRights': False,
                   'description': '',
                   'immutable': True,
                   'name': 'Full Access',
                   'rights': {'antiMalwareRights': {'antiMalwareConfigurationRights': {'canCreateNewAntiMalwareConfigurations': True,
                                                                                       'canDeleteAntiMalwareConfigurations': True,
                                                                                       'canEditAntiMalwareConfigurations': True},
                                                    'directoryListRights': {'canCreateNewDirectoryLists': True,
                                                                            'canDeleteDirectoryLists': True,
                                                                            'canEditDirectoryListProperties': True},
                                                    'fileExtensionListRights': {'canCreateNewFileExtensionLists': True,
                                                                                'canDeleteFileExtensionLists': True,
                                                                                'canEditFileExtensionListProperties': True},
                                                    'fileListRights': {'canCreateNewFileLists': True,
                                                                       'canDeleteFileLists': True,
                                                                       'canEditFileListProperties': True},
                                                    'identifiedFileRights': {'canDeleteIdentifiedFiles': True,
                                                                             'canDownloadIdentifiedFiles': True,
                                                                             'canRestoreIdentifiedFiles': True,
                                                                             'canSubmitIdentifiedFiles': True}},
                              'applicationControlRights': {'driftRights': {'canAllowOrBlockDrift': True,
                                                                           'canViewDrift': True},
                                                           'rulesetRights': {'canCreateNewRulesets': True,
                                                                             'canDeleteRulesets': True,
                                                                             'canEditRulesetProperties': True,
                                                                             'canViewRulesets': True},
                                                           'softwareInventoryRights': {'canCreateNewSoftwareInventory': True,
                                                                                       'canDeleteSoftwareInventory': True,
                                                                                       'canViewSoftwareInventory': True}},
                              'firewallRights': {'contextRights': {'canCreateNewContexts': True,
                                                                   'canDeleteContexts': True,
                                                                   'canEditContextProperties': True},
                                                 'firewallRuleRights': {'canCreateNewFirewallRules': True,
                                                                        'canDeleteFirewallRules': True,
                                                                        'canEditFirewallRuleProperties': True},
                                                 'macListRights': {'canCreateNewMACLists': True,
                                                                   'canDeleteMACLists': True,
                                                                   'canEditMACListProperties': True},
                                                 'statefulConfigurationRights': {'canCreateNewStatefulConfigurations': True,
                                                                                 'canDeleteStatefulConfigurations': True,
                                                                                 'canEditStatefulConfigurationProperties': True}},
                              'integrityMonitoringRights': {'integrityMonitoringRuleRights': {'canCreateNewIntegrityMonitoringRules': True,
                                                                                              'canDeleteIntegrityMonitoringRules': True,
                                                                                              'canEditIntegrityMonitoringRuleProperties': True}},
                              'intrusionPreventionRights': {'applicationTypeRights': {'canCreateNewApplicationTypes': True,
                                                                                      'canDeleteApplicationTypes': True,
                                                                                      'canEditApplicationTypeProperties': True},
                                                            'intrusionPreventionRuleRights': {'canCreateNewIntrusionPreventionRules': True,
                                                                                              'canDeleteIntrusionPreventionRules': True,
                                                                                              'canEditIntrusionPreventionRuleProperties': True}},
                              'logInspectionRights': {'logInspectionDecoderRights': {'canCreateNewLogInspectionDecoders': True,
                                                                                     'canDeleteLogInspectionDecoders': True,
                                                                                     'canEditLogInspectionDecoderProperties': True},
                                                      'logInspectionRuleRights': {'canCreateNewLogInspectionRules': True,
                                                                                  'canDeleteLogInspectionRules': True,
                                                                                  'canEditLogInspectionRuleProperties': True}},
                              'platformRights': {'administratorRights': {'canCreateNewAdministrators': True,
                                                                         'canDeleteAdministrators': True,
                                                                         'canEditAdministratorProperties': True,
                                                                         'canViewAdministrators': True},
                                                 'administratorRoleRights': {'canCreateNewAdministratorRoles': True,
                                                                             'canDeleteAdministratorRoles': True,
                                                                             'canEditAdministratorRoleProperties': True,
                                                                             'canViewAdministratorRoles': True},
                                                 'alertConfigurationRights': {'canEditAlertConfigurations': True},
                                                 'alertRights': {'canDismissGlobalAlerts': True},
                                                 'apikeyRights': {'canCreateNewApiKeys': True,
                                                                  'canDeleteApiKeys': True,
                                                                  'canEditApiKeyProperties': True,
                                                                  'canViewApiKeys': True},
                                                 'assetValueRights': {'canCreateNewAssetValues': True,
                                                                      'canDeleteAssetValues': True,
                                                                      'canEditAssetValueProperties': True},
                                                 'certificateRights': {'canCreateNewCertificates': True,
                                                                       'canDeleteCertificates': True},
                                                 'computerRights': {'canAddAndRemoveComputerGroups': True,
                                                                    'canCreateNewComputers': True,
                                                                    'canDeleteComputers': True,
                                                                    'canDismissAlerts': True,
                                                                    'canEditComputerProperties': True,
                                                                    'canImportComputers': True,
                                                                    'canManageCloudAccounts': True,
                                                                    'canManageDirectories': True,
                                                                    'canManageVCenters': True,
                                                                    'canTagComputers': True,
                                                                    'canViewNotRelatedToComputers': True,
                                                                    'canViewOtherComputers': True},
                                                 'contactRights': {'canCreateNewContacts': True,
                                                                   'canDeleteContacts': True,
                                                                   'canEditContactProperties': True,
                                                                   'canViewContacts': True},
                                                 'diagnosticRights': {'canCreateDiagnosticPackages': True},
                                                 'iplistRights': {'canCreateNewIPLists': True,
                                                                  'canDeleteIPLists': True,
                                                                  'canEditIPListProperties': True},
                                                 'licenseRights': {'canChangeLicense': True,
                                                                   'canViewLicense': True},
                                                 'multiTenantRights': {'canCreateAndEditTenantDatabaseServers': True,
                                                                       'canCreateTenants': True,
                                                                       'canDeleteTenantDatabaseServers': True,
                                                                       'canDeleteTenants': True,
                                                                       'canEditTenantAccountDetails': True,
                                                                       'canEditTenantFeatures': True,
                                                                       'canEditTenantGeneralProperties': True,
                                                                       'canEditTenantModules': True,
                                                                       'canEditTenantSettings': True,
                                                                       'canManageTenantAPIKeys': True,
                                                                       'canSignInAsTenant': True,
                                                                       'canViewTenants': True},
                                                 'policyRights': {'canCreateNewPolicies': True,
                                                                  'canDeletePolicies': True,
                                                                  'canEditPolicyProperties': True,
                                                                  'canImportPolicies': True,
                                                                  'canViewOtherPolicies': True},
                                                 'portListRights': {'canCreateNewPortLists': True,
                                                                    'canDeletePortLists': True,
                                                                    'canEditPortListProperties': True},
                                                 'proxyRights': {'canCreateNewProxies': True,
                                                                 'canDeleteProxies': True,
                                                                 'canEditProxyProperties': True},
                                                 'relayGroupRights': {'canCreateNewRelayGroups': True,
                                                                      'canDeleteRelayGroups': True,
                                                                      'canEditRelayGroupProperties': True},
                                                 'samlidentityProviderRights': {'canCreateNewSAMLIdentityProviders': True,
                                                                                'canDeleteSAMLIdentityProviders': True,
                                                                                'canEditSAMLIdentityProviders': True,
                                                                                'canViewSAMLIdentityProviders': True},
                                                 'scanCacheRights': {'canManageScanCache': True},
                                                 'scheduleRights': {'canCreateNewSchedules': True,
                                                                    'canDeleteSchedules': True,
                                                                    'canEditScheduleProperties': True},
                                                 'scheduledTaskRights': {'canCreateNewScheduledTasks': True,
                                                                         'canDeleteScheduledTasks': True,
                                                                         'canEditScheduledTaskProperties': True,
                                                                         'canExecuteScheduledTasks': True,
                                                                         'canViewScheduledTasks': True},
                                                 'settingRights': {'canEditSettings': True,
                                                                   'canViewSettings': True},
                                                 'syslogConfigurationRights': {'canCreateNewSyslogConfigurations': True,
                                                                               'canDeleteSyslogConfigurations': True,
                                                                               'canEditSyslogConfigurationProperties': True},
                                                 'systemInformationRights': {'canManageExtensions': True,
                                                                             'canManageNodes': True,
                                                                             'canViewSystemInformation': True},
                                                 'taggingRights': {'canDeleteAutoTagRules': True,
                                                                   'canDeleteTags': True,
                                                                   'canRunAutoTagRules': True,
                                                                   'canTag': True,
                                                                   'canUpdateAutoTagRules': True},
                                                 'updateRights': {'canDeleteRuleUpdates': True,
                                                                  'canDeleteSoftware': True,
                                                                  'canEditSoftwareProperties': True,
                                                                  'canImportRuleUpdates': True,
                                                                  'canImportSoftware': True,
                                                                  'canViewRuleUpdates': True}},
                              'webReputationRights': {'webReputationConfigurationRights': {'canEditWebReputationConfiguration': True}}},
                   'urn': 'urn:tmds:identity::0:role/Full Access'},
                {'ID': 2,
                   'allComputers': True,
                   'allPolicies': True,
                   'allowUserInterface': True,
                   'allowWebService': True,
                   'canOnlyManipulateUsersWithEqualOrLesserRights': False,
                   'description': '',
                   'immutable': False,
                   'name': 'Auditor',
                   'rights': {'antiMalwareRights': {'antiMalwareConfigurationRights': {'canCreateNewAntiMalwareConfigurations': False,
                                                                                       'canDeleteAntiMalwareConfigurations': False,
                                                                                       'canEditAntiMalwareConfigurations': False},
                                                    'directoryListRights': {'canCreateNewDirectoryLists': False,
                                                                            'canDeleteDirectoryLists': False,
                                                                            'canEditDirectoryListProperties': False},
                                                    'fileExtensionListRights': {'canCreateNewFileExtensionLists': False,
                                                                                'canDeleteFileExtensionLists': False,
                                                                                'canEditFileExtensionListProperties': False},
                                                    'fileListRights': {'canCreateNewFileLists': False,
                                                                       'canDeleteFileLists': False,
                                                                       'canEditFileListProperties': False},
                                                    'identifiedFileRights': {'canDeleteIdentifiedFiles': False,
                                                                             'canDownloadIdentifiedFiles': False,
                                                                             'canRestoreIdentifiedFiles': False,
                                                                             'canSubmitIdentifiedFiles': False}},
                              'applicationControlRights': {'driftRights': {'canAllowOrBlockDrift': False,
                                                                           'canViewDrift': False},
                                                           'rulesetRights': {'canCreateNewRulesets': False,
                                                                             'canDeleteRulesets': False,
                                                                             'canEditRulesetProperties': False,
                                                                             'canViewRulesets': False},
                                                           'softwareInventoryRights': {'canCreateNewSoftwareInventory': False,
                                                                                       'canDeleteSoftwareInventory': False,
                                                                                       'canViewSoftwareInventory': False}},
                              'firewallRights': {'contextRights': {'canCreateNewContexts': False,
                                                                   'canDeleteContexts': False,
                                                                   'canEditContextProperties': False},
                                                 'firewallRuleRights': {'canCreateNewFirewallRules': False,
                                                                        'canDeleteFirewallRules': False,
                                                                        'canEditFirewallRuleProperties': False},
                                                 'macListRights': {'canCreateNewMACLists': False,
                                                                   'canDeleteMACLists': False,
                                                                   'canEditMACListProperties': False},
                                                 'statefulConfigurationRights': {'canCreateNewStatefulConfigurations': False,
                                                                                 'canDeleteStatefulConfigurations': False,
                                                                                 'canEditStatefulConfigurationProperties': False}},
                              'integrityMonitoringRights': {'integrityMonitoringRuleRights': {'canCreateNewIntegrityMonitoringRules': False,
                                                                                              'canDeleteIntegrityMonitoringRules': False,
                                                                                              'canEditIntegrityMonitoringRuleProperties': False}},
                              'intrusionPreventionRights': {'applicationTypeRights': {'canCreateNewApplicationTypes': False,
                                                                                      'canDeleteApplicationTypes': False,
                                                                                      'canEditApplicationTypeProperties': False},
                                                            'intrusionPreventionRuleRights': {'canCreateNewIntrusionPreventionRules': False,
                                                                                              'canDeleteIntrusionPreventionRules': False,
                                                                                              'canEditIntrusionPreventionRuleProperties': False}},
                              'logInspectionRights': {'logInspectionDecoderRights': {'canCreateNewLogInspectionDecoders': False,
                                                                                     'canDeleteLogInspectionDecoders': False,
                                                                                     'canEditLogInspectionDecoderProperties': False},
                                                      'logInspectionRuleRights': {'canCreateNewLogInspectionRules': False,
                                                                                  'canDeleteLogInspectionRules': False,
                                                                                  'canEditLogInspectionRuleProperties': False}},
                              'platformRights': {'administratorRights': {'canCreateNewAdministrators': False,
                                                                         'canDeleteAdministrators': False,
                                                                         'canEditAdministratorProperties': False,
                                                                         'canViewAdministrators': False},
                                                 'administratorRoleRights': {'canCreateNewAdministratorRoles': False,
                                                                             'canDeleteAdministratorRoles': False,
                                                                             'canEditAdministratorRoleProperties': False,
                                                                             'canViewAdministratorRoles': False},
                                                 'alertConfigurationRights': {'canEditAlertConfigurations': False},
                                                 'alertRights': {'canDismissGlobalAlerts': False},
                                                 'apikeyRights': {'canCreateNewApiKeys': False,
                                                                  'canDeleteApiKeys': False,
                                                                  'canEditApiKeyProperties': False,
                                                                  'canViewApiKeys': False},
                                                 'assetValueRights': {'canCreateNewAssetValues': False,
                                                                      'canDeleteAssetValues': False,
                                                                      'canEditAssetValueProperties': False},
                                                 'certificateRights': {'canCreateNewCertificates': False,
                                                                       'canDeleteCertificates': False},
                                                 'computerRights': {'canAddAndRemoveComputerGroups': False,
                                                                    'canCreateNewComputers': False,
                                                                    'canDeleteComputers': False,
                                                                    'canDismissAlerts': False,
                                                                    'canEditComputerProperties': False,
                                                                    'canImportComputers': False,
                                                                    'canManageCloudAccounts': False,
                                                                    'canManageDirectories': False,
                                                                    'canManageVCenters': False,
                                                                    'canTagComputers': False,
                                                                    'canViewNotRelatedToComputers': True,
                                                                    'canViewOtherComputers': True},
                                                 'contactRights': {'canCreateNewContacts': False,
                                                                   'canDeleteContacts': False,
                                                                   'canEditContactProperties': False,
                                                                   'canViewContacts': False},
                                                 'diagnosticRights': {'canCreateDiagnosticPackages': False},
                                                 'iplistRights': {'canCreateNewIPLists': False,
                                                                  'canDeleteIPLists': False,
                                                                  'canEditIPListProperties': False},
                                                 'licenseRights': {'canChangeLicense': False,
                                                                   'canViewLicense': False},
                                                 'multiTenantRights': {'canCreateAndEditTenantDatabaseServers': False,
                                                                       'canCreateTenants': False,
                                                                       'canDeleteTenantDatabaseServers': False,
                                                                       'canDeleteTenants': False,
                                                                       'canEditTenantAccountDetails': False,
                                                                       'canEditTenantFeatures': False,
                                                                       'canEditTenantGeneralProperties': False,
                                                                       'canEditTenantModules': False,
                                                                       'canEditTenantSettings': False,
                                                                       'canManageTenantAPIKeys': False,
                                                                       'canSignInAsTenant': False,
                                                                       'canViewTenants': False},
                                                 'policyRights': {'canCreateNewPolicies': False,
                                                                  'canDeletePolicies': False,
                                                                  'canEditPolicyProperties': False,
                                                                  'canImportPolicies': False,
                                                                  'canViewOtherPolicies': True},
                                                 'portListRights': {'canCreateNewPortLists': False,
                                                                    'canDeletePortLists': False,
                                                                    'canEditPortListProperties': False},
                                                 'proxyRights': {'canCreateNewProxies': False,
                                                                 'canDeleteProxies': False,
                                                                 'canEditProxyProperties': False},
                                                 'relayGroupRights': {'canCreateNewRelayGroups': False,
                                                                      'canDeleteRelayGroups': False,
                                                                      'canEditRelayGroupProperties': False},
                                                 'samlidentityProviderRights': {'canCreateNewSAMLIdentityProviders': False,
                                                                                'canDeleteSAMLIdentityProviders': False,
                                                                                'canEditSAMLIdentityProviders': False,
                                                                                'canViewSAMLIdentityProviders': False},
                                                 'scanCacheRights': {'canManageScanCache': False},
                                                 'scheduleRights': {'canCreateNewSchedules': False,
                                                                    'canDeleteSchedules': False,
                                                                    'canEditScheduleProperties': False},
                                                 'scheduledTaskRights': {'canCreateNewScheduledTasks': False,
                                                                         'canDeleteScheduledTasks': False,
                                                                         'canEditScheduledTaskProperties': False,
                                                                         'canExecuteScheduledTasks': False,
                                                                         'canViewScheduledTasks': False},
                                                 'settingRights': {'canEditSettings': False,
                                                                   'canViewSettings': False},
                                                 'syslogConfigurationRights': {'canCreateNewSyslogConfigurations': False,
                                                                               'canDeleteSyslogConfigurations': False,
                                                                               'canEditSyslogConfigurationProperties': False},
                                                 'systemInformationRights': {'canManageExtensions': False,
                                                                             'canManageNodes': False,
                                                                             'canViewSystemInformation': False},
                                                 'taggingRights': {'canDeleteAutoTagRules': False,
                                                                   'canDeleteTags': False,
                                                                   'canRunAutoTagRules': False,
                                                                   'canTag': False,
                                                                   'canUpdateAutoTagRules': False},
                                                 'updateRights': {'canDeleteRuleUpdates': False,
                                                                  'canDeleteSoftware': False,
                                                                  'canEditSoftwareProperties': False,
                                                                  'canImportRuleUpdates': False,
                                                                  'canImportSoftware': False,
                                                                  'canViewRuleUpdates': False}},
                              'webReputationRights': {'webReputationConfigurationRights': {'canEditWebReputationConfiguration': False}}},
                   'urn': 'urn:tmds:identity::0:role/Auditor'}]
        self.roles = roles
        return self.roles

    def get_api_keys_info(self):

        api_keys = [
                    {'ID': 2,
                    'active': True,
                    'created': 1564452888620,
                    'description': '',
                    'keyName': 'test',
                    'locale': 'ja-JP',
                    'roleID': 1,
                    'serviceAccount': False,
                    'timeZone': 'Asia/Tokyo',
                    'unsuccessfulSignInAttempts': 0},
                    {'ID': 3,
                    'active': True,
                    'created': 1564455073500,
                    'description': '',
                    'keyName': 'test2',
                    'locale': 'ja-JP',
                    'roleID': 2,
                    'serviceAccount': False,
                    'timeZone': 'Asia/Tokyo',
                    'unsuccessfulSignInAttempts': 0},
                    {'ID': 8,
                    'active': True,
                    'created': 1564531123197,
                    'description': '',
                    'keyName': 'test3',
                    'locale': 'ja-JP',
                    'roleID': 3,
                    'serviceAccount': False,
                    'timeZone': 'Asia/Tokyo',
                    'unsuccessfulSignInAttempts': 0},
                    {'ID': 9,
                    'active': True,
                    'created': 1564531411137,
                    'description': '',
                    'keyName': 'test4',
                    'locale': 'ja-JP',
                    'roleID': 1,
                    'serviceAccount': False,
                    'timeZone': 'Asia/Tokyo',
                    'unsuccessfulSignInAttempts': 0}]
        self.api_keys = api_keys
        return self.api_keys


"""
tkinterの枠作成
"""

def create_frame(root):
    f0 = ttk.LabelFrame(root, width=250, height=200, text='Users')
    f1 = ttk.LabelFrame(root, width=250, height=200, text='Roles')
    f2 = ttk.LabelFrame(root, width=250, height=200, text='API keys')
    f3 = ttk.LabelFrame(root, width=100, height=200, text='Settings')

    f0.grid(padx = 5, pady = 5, ipadx = 5, ipady = 5)
    f0.columnconfigure(0, weight=1)
    f0.rowconfigure(0, weight=1)
    f0.grid_propagate(False)

    f1.grid(row=0, column=1, padx = 5, pady = 5, ipadx = 5, ipady = 5)
    f1.columnconfigure(0, weight=1)
    f1.rowconfigure(0, weight=1)
    f1.grid_propagate(False)

    f2.grid(row=0, column=2, padx = 5, pady = 5, ipadx = 5, ipady = 5)
    f2.columnconfigure(0, weight=1)
    f2.rowconfigure(0, weight=1)
    f2.grid_propagate(False)

    f3.grid(row=0, column=3, padx = 5, pady = 5, ipadx = 5, ipady = 5)
    f3.columnconfigure(0, weight=1)
    f3.grid_propagate(False)

    button0 = ttk.Button(f3, text='Get Info')
    button1 = ttk.Button(f3, text='Create Users', command=create_user_window)
    button2 = ttk.Button(f3, text='Create Roles', command=create_role_window)
    button3 = ttk.Button(f3, text='Create API keys', command=create_apikey_window)

    button0.grid(row=1, column=0, sticky='EW')
    button1.grid(row=2, column=0, sticky='EW')
    button2.grid(row=3, column=0, sticky='EW')
    button3.grid(row=4, column=0, sticky='EW')


    tree0 = ttk.Treeview(f0)
    tree0["columns"]=(1,2,3)
    tree0.heading("#0", text="")
    tree0.heading(1, text="item")
    tree0.heading(2, text="value")

    tree0.column("#0", minwidth=50, stretch=False, width=100)
    tree0.column(1, minwidth=50, stretch=False, width=50)
    tree0.column(2, minwidth=50, stretch=False, width=50)

    xScrollbar = ttk.Scrollbar(f0, orient='horizontal', command=tree0.xview)
    xScrollbar.config(command=tree0.xview)
    yScrollbar = ttk.Scrollbar(f0, orient='vertical', command=tree0.yview)
    yScrollbar.config(command=tree0.yview)
    tree0.config(xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)

    tree0.grid(row=0, column=0, sticky='NEWS')
    xScrollbar.grid(row=1, column=0, sticky='EW')
    yScrollbar.grid(row=0, column=1, sticky='NS')


    tree1 = ttk.Treeview(f1)
    tree1["columns"]=(1,2,3)
    tree1.heading("#0", text="")
    tree1.heading(1, text="item")
    tree1.heading(2, text="value")

    tree1.column("#0", minwidth=50, stretch=False, width=100)
    tree1.column(1, minwidth=50, stretch=False, width=50)
    tree1.column(2, minwidth=50, stretch=False, width=50)

    xScrollbar1 = ttk.Scrollbar(f1, orient='horizontal')
    xScrollbar1.config(command=tree1.xview)

    yScrollbar1 = ttk.Scrollbar(f1, orient='vertical', command=tree1.yview)
    yScrollbar1.config(command=tree1.yview)

    tree1.config(xscrollcommand=xScrollbar1.set, yscrollcommand=yScrollbar1.set)

    tree1.grid(row=0, column=0, sticky='NEWS')
    xScrollbar1.grid(row=1, column=0, sticky='EW')
    yScrollbar1.grid(row=0, column=1, sticky='NS')


    tree2 = ttk.Treeview(f2)
    tree2["columns"]=(1,2,3)
    tree2.heading("#0", text="")
    tree2.heading(1, text="item")
    tree2.heading(2, text="value")

    tree2.column("#0", minwidth=50, stretch=False, width=100)
    tree2.column(1, minwidth=50, stretch=False, width=50)
    tree2.column(2, minwidth=50, stretch=False, width=50)

    xScrollbar2 = ttk.Scrollbar(f2, orient='horizontal')
    xScrollbar2.config(command=tree2.xview)

    yScrollbar2 = ttk.Scrollbar(f2, orient='vertical', command=tree2.yview)
    yScrollbar2.config(command=tree1.yview)

    tree2.config(xscrollcommand=xScrollbar2.set, yscrollcommand=yScrollbar2.set)

    tree2.grid(row=0, column=0, sticky='NEWS')
    xScrollbar2.grid(row=1, column=0, sticky='EW')
    yScrollbar2.grid(row=0, column=1, sticky='NS')

    return tree0, tree1, tree2

def create_user_window():
    #サブウィンドウ作成
    sub_win = tkinter.Toplevel()

    #サブウィンドウの画面サイズ
    sub_win.geometry("400x400")

    #サブウィンドウのcanvas
    canvas = tkinter.Canvas(sub_win, width=365, height=365)
    canvas.grid()

    #サブウィンドウ canvasのスクロールバー
    xScrollbar = tkinter.Scrollbar(sub_win, orient='horizontal')
    xScrollbar.grid(row=1, column=0, sticky='EW')
    xScrollbar.config(command=canvas.xview) 

    yScrollbar = tkinter.Scrollbar(sub_win, orient='vertical')
    yScrollbar.grid(row=0, column=1, sticky='NS')
    yScrollbar.config(command=canvas.yview)   

    #サブウィンドウ canvasの配置
    canvas.config(xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)
    canvas.config(scrollregion=(0,0,800,800))

    #サブウィンドウのframe
    sub_win_frame = tkinter.Frame(canvas)
    #sub_win_frame.grid(row=0, column=0)
    canvas.create_window(0,0, window=sub_win_frame, anchor='nw')

    user_item =[
                'username',
                'password',
                'fullName',
                'description',
                'roleID',
                'locale',
                'timeZone',
                'timeFormat',
                'passwordNeverExpires',
                'active',
                'mfaType',
                'phoneNumber',
                'mobileNumber',
                'pagerNumber',
                'emailAddress',
                'primaryContact',
                'receiveNotifications',
                'reportPDFPasswordEnabled',
                'reportPDFPassword',
                'UTCOffset'
                ]
    item_length = len(user_item)
    sub_win_entry = [''] * item_length
    sub_win_label = [''] * item_length

    for x in range(item_length):
        sub_win_entry[x] = ttk.Entry(sub_win_frame, width=10)
        sub_win_label[x] = ttk.Label(sub_win_frame, text=user_item[x])

        sub_win_label[x].grid(row=x, column=0)
        sub_win_entry[x].grid(row=x, column=1)

    #サブウィンドウのボタン生成
    sub_win_button = ttk.Button(
                                        sub_win_frame,
                                        text="Create",
                                        width=str("Create"),
                                        command=sub_win.destroy
                                    )
    sub_win_button.grid(row=item_length + 1, column=1)


def create_role_window():
    #サブウィンドウ作成
    sub_win = tkinter.Toplevel()

    #サブウィンドウの画面サイズ
    sub_win.geometry("400x400")

    #サブウィンドウのcanvas
    canvas = tkinter.Canvas(sub_win, width=365, height=365)
    canvas.grid()

    #サブウィンドウ canvasのスクロールバー
    xScrollbar = tkinter.Scrollbar(sub_win, orient='horizontal')
    xScrollbar.grid(row=1, column=0, sticky='EW')
    xScrollbar.config(command=canvas.xview) 

    yScrollbar = tkinter.Scrollbar(sub_win, orient='vertical')
    yScrollbar.grid(row=0, column=1, sticky='NS')
    yScrollbar.config(command=canvas.yview)   

    #サブウィンドウ canvasの配置
    canvas.config(xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)
    canvas.config(scrollregion=(0,0,800,800))

    #サブウィンドウのframe
    sub_win_frame = tkinter.Frame(canvas)
    #sub_win_frame.grid(row=0, column=0)
    canvas.create_window(0,0, window=sub_win_frame, anchor='nw')
    

    user_item =[
                'name',
                'description',
                'canOnlyManipulateUsersWithEqualOrLesserRights',
                'allComputers',
                'allPolicies',
                'allowUserInterface',
                'allowWebService',
                'rights',
                'computerIDs',
                'computerGroupIDs',
                'policyIDs'
                ]
    item_length = len(user_item)
    sub_win_entry = [''] * item_length
    sub_win_label = [''] * item_length

    for x in range(item_length):
        sub_win_entry[x] = ttk.Entry(sub_win_frame, width=10)
        sub_win_label[x] = ttk.Label(sub_win_frame, text=user_item[x])

        sub_win_label[x].grid(row=x, column=0)
        sub_win_entry[x].grid(row=x, column=1)

    #サブウィンドウのボタン生成
    sub_win_button = ttk.Button(
                                        sub_win_frame,
                                        text="Create",
                                        width=str("Create"),
                                        command=sub_win.destroy
                                    )
    sub_win_button.grid(row=item_length + 1, column=1)


def create_apikey_window():
    #サブウィンドウ作成
    sub_win = tkinter.Toplevel()

    #サブウィンドウの画面サイズ
    sub_win.geometry("400x400")

    #サブウィンドウのcanvas
    canvas = tkinter.Canvas(sub_win, width=365, height=365)
    canvas.grid()

    #サブウィンドウ canvasのスクロールバー
    xScrollbar = tkinter.Scrollbar(sub_win, orient='horizontal')
    xScrollbar.grid(row=1, column=0, sticky='EW')
    xScrollbar.config(command=canvas.xview) 

    yScrollbar = tkinter.Scrollbar(sub_win, orient='vertical')
    yScrollbar.grid(row=0, column=1, sticky='NS')
    yScrollbar.config(command=canvas.yview)   

    #サブウィンドウ canvasの配置
    canvas.config(xscrollcommand=xScrollbar.set, yscrollcommand=yScrollbar.set)
    canvas.config(scrollregion=(0,0,800,800))

    #サブウィンドウのframe
    sub_win_frame = tkinter.Frame(canvas)
    #sub_win_frame.grid(row=0, column=0)
    canvas.create_window(0,0, window=sub_win_frame, anchor='nw')

    user_item =[
                'keyName',
                'description',
                'locale',
                'roleID',
                'timeZone',
                'active',
                'created',
                'lastSignIn',
                'unlockTime',
                'unsuccessfulSignInAttempts',
                'expiryDate'
                ]
    item_length = len(user_item)
    sub_win_entry = [''] * item_length
    sub_win_label = [''] * item_length

    for x in range(item_length):
        sub_win_entry[x] = ttk.Entry(sub_win_frame, width=10)
        sub_win_label[x] = ttk.Label(sub_win_frame, text=user_item[x])

        sub_win_label[x].grid(row=x, column=0)
        sub_win_entry[x].grid(row=x, column=1)

    #サブウィンドウのボタン生成
    sub_win_button = ttk.Button(
                                        sub_win_frame,
                                        text="Create",
                                        width=str("Create"),
                                        command=sub_win.destroy
                                    )
    sub_win_button.grid(row=item_length + 1, column=1)



'''
上の行までで枠が完成
以降はtreeの設定、insert
'''

def tree_insert(tree0, tree1, tree2, user_data, role_data, apikey_data):

    def get_keys(target_dict):
        for key, value in target_dict.items():
            if not isinstance (value, dict):
                yield key
            else:
                for child in get_keys(value):
                    yield key + '.' + child

    def get_value(target_dict, target_branch):
        limbs = target_branch.split('.')
        leaf = target_dict
        for one_limb in limbs:
            leaf = leaf[one_limb]
        return one_limb, leaf

    for x in range(len(user_data)):
        root_node = tree0.insert(
            "",     #最上位なのでparentは空文字
            "end",
            text=user_data[x]['username'],
            )
        #辞書の要素を挿入
        for y in list(get_keys(user_data[x])):
            value = get_value(user_data[x], y)
            tree0.insert(
                root_node,  #parentはキーの認識番号
                "end",
                values = (value[0], value[1]),
                )

    for x in range(len(role_data)):
        root_node = tree1.insert(
            "",     #最上位なのでparentは空文字
            "end",
            text=role_data[x]['name'],
            )
        #辞書の要素を挿入
        for y in list(get_keys(role_data[x])):
            value = get_value(role_data[x], y)
            tree1.insert(
                root_node,  #parentはキーの認識番号
                "end",
                values = (value[0], value[1]),
                )

    for x in range(len(apikey_data)):
        root_node = tree2.insert(
            "",     #最上位なのでparentは空文字
            "end",
            text=apikey_data[x]['keyName'],
            )
        #辞書の要素を挿入
        for y, z in apikey_data[x].items():
            tree2.insert(
                root_node,  #parentはキーの認識番号
                "end",
                values = (y, z)
                )


def main():
    root = tkinter.Tk()
    root.title('DS Tool')
    root.geometry('950x300')

    host = "https://54.250.246.185:4119/api/"
    api_secret_key = "aaaa"

    data = get_info(host, api_secret_key)

    user_data = data.get_users_info()
    role_data = data.get_roles_info()
    apikey_data = data.get_api_keys_info()

    result = create_frame(root)
    #create_user_window()
    #create_role_window()
    #create_apikey_window()

    tree_insert(result[0], result[1], result[2], user_data, role_data, apikey_data)

    #最後に
    root.mainloop()


if __name__ == '__main__':
    main()