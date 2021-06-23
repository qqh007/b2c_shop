# 购物系统

## 简介

实现了一个12个实体的购物商城系统

分为商家端和用户端

数据库：MySQL

后端开发：Django+Python

前端开发：Bootstrap+Html+JavaScript

## 效果展示

导航栏

![](图片展示/导航栏.png)

图 导航栏



除此之外，我们还实现了模态框和图片轮播功能。

模态框可以提供用户编辑数据或者提醒，独立于页面而存在，可以提供信息和交互。

![](图片展示/模态框.png)

图 模态框



图片轮播可以作为广告位，让我们的页面看起来非常的精美。



![](图片展示/图片轮播.png)

图 图片轮播

## 系统实现效果

### 用户端

#### 登录

![](图片展示/登录界面.png)

#### 注册

![](图片展示/注册界面.png)

#### 商城主界面

![](图片展示/商城主界面.png)



#### 产品主界面

![](图片展示/产品主界面.png)

#### 商家主界面

![](图片展示/店铺页面.png)

#### 查看评论

![](图片展示/商品评价.png)

#### 购物车

![](图片展示/购物车.png)

可以对购物车里面的数量进行加减操作和删除操作，下方会实时显示当前合计。

#### 收藏夹

![](图片展示/收藏夹.png)

#### 浏览记录

![](图片展示/浏览记录.png)

#### 消息

![](图片展示/用户消息.png)

在商家发货时或者发布优惠券时等情况，商家会给用户发送一条消息来提醒用户

#### 订单页面

![](图片展示/订单页面.png)

订单页面分为4个部分，是根据订单的状态来划分的。

用户可以确认收货。

![](图片展示/确认收货.png)

用户可以对已经收货的商品进行评价。

![](图片展示/评价订单.png)

#### 个人主页

用户可以进行修改头像，编辑资料和修改密码的操作。

![](图片展示/个人主页.png)

#### 地址页面

![](图片展示/地址页面.png)

通过点击按钮，用户可以新增或编辑地址。

![](图片展示/新增地址.png)

#### 结算界面

用户可以选择收货地址，被选中的地址会改变样式。

在选择收货地址的同时，用户需要确认商品信息。

![](图片展示/结算界面.png)

### 商家端

#### 登录和注册

和用户界面大致相同

#### 完善信息

商家第一次登陆需要完善自己的店铺信息。

![](图片展示/店铺/完善信息.png)

#### 管理商品

商家可以进行编辑、查看详情、上架或下架、发布优惠券和删除删除这些操作。

![](图片展示/店铺/管理商品.png)

#### 管理商品类别

![](图片展示/店铺/管理商品类别.png)

#### 管理订单

商家可以发货，还可以提醒已收货但未评价的用户评价订单。

![](图片展示/店铺/管理订单.png)

#### 管理优惠券

![](图片展示/店铺/管理优惠券.png)

#### 管理消息

买家在下单收货的时候会发送一条消息提示商家。

![](图片展示/店铺/管理消息.png)

#### 销售情况

销售情况分为了三个模块：

销量展示、销售额汇总和店铺信息变化。

![](图片展示/店铺/销售情况.png)

#### 商品销量展示

在销量展示页面，商家可以看到本店的商品销量情况。

销售情况以饼状图的样式展现。

![](图片展示/店铺/销量展示.png)

#### 店铺销售额汇总

在店铺销售额汇总页面，商家可以看到所有注册商家的销售额情况。

销售额情况以柱状图的样式展现。

![](图片展示/店铺/店铺销售额汇总.png)

#### 店铺信息变化

在店铺信息变化页面，商家可以看到本店的销售额变化情况和关注本店的人数变化情况。

店铺信息变化情况以折线图的形式展现。

![](图片展示/店铺/店铺信息变化.png)