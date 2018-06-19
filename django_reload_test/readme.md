关于django项目热部署问题：
	1.不需要重启服务，直接覆盖文件，django会自动重启
	2.取消django的reload 针对django的web服务可以添加 –noreload参数