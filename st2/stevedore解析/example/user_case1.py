from stevedore import driver
mgr = driver.DriverManager(
    namespace='stevedore.formatter',
    name='simple',
    invoke_on_load=True
) # 加载组名或者说命名空间为stevedore.formetter下name为simple的插件
st = mgr.driver.format({'caesa':'sss'})
data = mgr.driver.data # mgr.driver实例化simple对象并调用其data属性
print(data)
