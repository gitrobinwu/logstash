#-*- coding:utf-8 -*-
# 设置security-*底层模板	
body = {
	"order": 0,
	"template": "security-*",
	"settings": {
		"number_of_shards": 5,
		"number_of_replicas":0,
		"refresg_interval": "5s"
	},
	"aliases":{
		"security-log": {}
	},
	"mappings": {
		"_default_": {
			"_all": {
				"omit_norms": "true",
				"enabled": "true"
			},
			"numeric_detection":"true",
			"dynamic_templates": [
			{
				"string_fields": {
					"mapping": {
						"fielddata": {
							"format": "disabled"
						},
						"index": "analyzed",
						"omit_norms": "true",
						"type": "string",
						"fields": {
							"raw": {
								"ignore_above": 256,
								"index": "not_analyzed",
								"type": "string",
								"doc_values": "true"
							}
						}
					},
					"match_mapping_type": "string",
					"match": "*"
				}	
			},
			{
				"float_fields": {
					"match": "*",
					"match_mapping_type": "float",
					"mapping": {
						"type": "float",
						"doc_values": "true"
					}
				}
			},
			{
				"double_fields": {
					"match": "*",
					"match_mapping_type": "double",
					"mapping": {
						"type": "double",
						"doc_values": "true"
					}
				}
			},
			{
				"date_fields": {
					"match": "*",
					"match_mapping_type": "date",
					"mapping":{
						"type": "date",
						"doc_values": "true"
					}
				}
			},
			{
				"long_fields": {
					"match": "*",
					"match_mapping_type": "long",
					"mapping": {
						"type": "long",
						"doc_values": "true"
					}
				}
			}
			],
			"properties": {
				"@timestamp": {
					"type": "date",
					"doc_values": "true"
				},
				"@version": {
					"index": "not_analyzed",
					"type": "string",
					"doc_values": "true"
				},
				"host": {
					"type": "string",
					"index": "not_analyzed"
				}
			}
		}
	}
}	

#账户成功登录模板
success_login = {
	"order": 1,
	"template": "security-success-login-*",
	"mappings": {
		"success-login": {
			"properties": {
				"event_id": {
					"type": "integer",
					"doc_values": "true"
				},
				"login_type": {
					"type": "integer",
					"doc_values": "true"
				},
				"account_name": {
					"type": "string",
					"index": "not_analyzed",
					"doc_values": "true"
				},
				"account_domain": {
					"type": "string",
					"index": "not_analyzed",
					"doc_values": "true"
				}
			}
		}
	}
}


#账户登录失败模板
failed_login = {
	"order": 1,
	"template": "security-failed-login-*",
	"mappings": {
		"failed-login": {
			"properties": {
				"event_id": {
					"type": "integer",
					"doc_values": "true"
				},
				"login_type": {
					"type": "integer",
					"doc_values": "true"
				},
				"account_name": {
					"type": "string",
					"index": "not_analyzed",
					"doc_values": "true"
				},
				"account_domain": {
					"type": "string",
					"index": "not_analyzed",
					"doc_values": "true"
				}
			}
		}
	}
}

#已注销账户模板
close_account = {
	"order": 1,
	"template": "security-close-account-*",
	"mappings": {
		"close-account": {
			"properties": {
				"event_id": {
					"type": "integer",
					"doc_values": "true"
				},
				"login_type": {
					"type": "integer",
					"doc_values": "true"
				},
				"account_name": {
					"type": "string",
					"index": "not_analyzed",
					"doc_values": "true"
				},
				"account_domain": {
					"type": "string",
					"index": "not_analyzed",
					"doc_values": "true"
				},
				"login_id": {
					"type": "string",
					"index": "not_analyzed",
					"doc_values": "true"
				}
			}
		}
	}
}
