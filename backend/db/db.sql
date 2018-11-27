create database db_gp default character set utf8;

use db_gp;

create table tab_com_infos(
	ci_id bigint auto_increment comment '商品id',
	ci_title varchar(30) not null comment '商品标题',			##前端要求：10字以内
	ci_infos varchar(1500) not null comment '商品描述',			##前端要求：500字以内
	ci_oprice bigint not null comment '商品原价',				##以分为单位
	ci_nprice bigint not null comment '商品价格'	,				
	ci_sales bigint not null default 0 comment '商品销量',
	ci_freight bigint default 0 comment '商品运费',
	ci_class int not null comment '商品分类',					#1：零食 2：水果 3：小吃 4：手工 5：其他
	ci_img varchar(64) not null comment '商品图片名称',
	ci_specifications varchar(15) not null comment '商品规格',
	ci_excellent int default 0 comment '优质商品',				#1：是 0：不是	优质商品展示在首页轮播图,最多5个
	ci_hot int default 0 comment '热销商品', 					#1:是 0：不是 	热销商品展示首页,有且只能有2个
	PRIMARY KEY (ci_id),
	unique(ci_id)
) engine=InnoDB default charset=utf8 comment '商品表';


create table tab_user_infos(
	ui_id bigint auto_increment comment '用户id',
	ui_number varchar(12) not null comment '用户账号',
	ui_name varchar(24) not null comment '用户名',					#前端要求:8个字内
	ui_salt varchar(64) not null comment '用户新建时产生的密文',
	ui_pic varchar(64) not null default 'userPic.png' comment '用户头像',
	ui_sex int not null default 1 comment '用户性别',				#1:男 2：女
	ui_address varchar(140) comment '收货地址',
	ui_mailbox varchar(72) not null comment '用户邮箱',
	ui_identity int default 2 comment '用户身份',		#0：root,1:管理员，2：普通用户 3:异常用户
	PRIMARY KEY (ui_id),
	unique(ui_number)
) engine=InnoDB default charset=utf8 comment '用户表';

create table tab_order_infos(
	oi_id bigint auto_increment comment '订单id',
	oi_uid bigint not null comment '用户id',
	oi_cid bigint not null comment '商品id',
	oi_num int not null default 1 comment '商品数量',		#当添加购物车商品重复时,直接更改数量即可
	oi_state int not null comment '商品状态', 	#0:购物车 1:未付款 2：已付款
	oi_price bigint comment '购买时价格',		#此字段应该在付款成功后更新状态时填入
	oi_utime datetime not null default current_timestamp on update current_timestamp comment '最后更新时间',
	oi_number bigint not null comment '订单编号',
	foreign key(oi_uid) references tab_user_infos(ui_id),
	foreign key(oi_cid) references tab_com_infos(ci_id),
	PRIMARY KEY (oi_id),
	unique(oi_id)
)engine=InnoDB default charset=utf8 comment '订单表';


#插入默认用户root
insert into tab_user_infos (ui_number,ui_name,ui_salt,ui_mailbox,ui_identity) values ('root','超级管理员','b86f0e6db1374e271b5408ce3b42903c194cd8efc9192fca5606f95960f1ee5f','1209799738@qq.com',0);

