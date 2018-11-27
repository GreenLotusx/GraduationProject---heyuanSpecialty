from tornado.web import StaticFileHandler
from handlers.loginhandler import checkLoginHandler, loginHandler, logoutHandler,registerHandler
from handlers.userhandler import setUserInfosHandler, getUserInfosHandler,setUserAddressHandler,setUserPasswordHandler
from handlers.commodityHandler import commodityDataHandler,manyCommodityHandler,queryLikeCommodityHandler
from handlers.commodityHandler import addCommodityHandler,updateCommodityHandler,deleteCommodityHandler
from handlers.commodityHandler import queryIndexHandler,queryClassCommodityHandler,recommendCommoditiesHandler
from handlers.buyHandler import addCartHandler,queryCartHandler,queryManyHandler,deleteCartHandler,orderHandler,payHandler,queryOrderHandler
from app import config

urls = [
        (r"/api/check_login", checkLoginHandler.CheckLoginHandler),
        (r"/api/login", loginHandler.LoginHandler),
        (r"/api/logout", logoutHandler.LogoutHandler),
        (r"/api/user_infos", getUserInfosHandler.UserInfosHandler),
        (r"/api/set_infos", setUserInfosHandler.SetUserInfosHandler),
        (r"/api/set_address",setUserAddressHandler.SetUserAddressHandler),
        (r"/api/set_pwd",setUserPasswordHandler.SetUserPasswordHandler),
        (r"/api/register",registerHandler.RegisterHandler),
        (r"/api/commodity_data",commodityDataHandler.CommodityDataHandler),
        (r"/api/many_commodity",manyCommodityHandler.ManyCommodityHandler),
        (r"/api/query_like",queryLikeCommodityHandler.QueryLikeCommodityHandler),
        (r"/api/query_class", queryClassCommodityHandler.QueryClassCommodityHandler),
        (r"/api/add_commodity",addCommodityHandler.AddCommodityHandler),
        (r"/api/update_commodity", updateCommodityHandler.UpdateCommodityHandler),
        (r"/api/delete_commodity",deleteCommodityHandler.DeleteCommodityHandler),
        (r"/api/index_data",queryIndexHandler.QueryIndexHandler),
        (r"/api/rec_commodities",recommendCommoditiesHandler.RecommendCommoditiesHandler),
        (r"/api/add_cart",addCartHandler.AddCartHandler),
        (r"/api/query_cart",queryCartHandler.QueryCartHandler),
        (r"/api/query_many",queryManyHandler.QueryManyHandler),
        (r"/api/delete_cart",deleteCartHandler.DeleteCartHandler),
        (r"/api/order",orderHandler.OrderHandler),
        (r"/api/pay",payHandler.PayHandler),
        (r"/api/query_order",queryOrderHandler.QueryOrderHandler),
        (r"/(.*)",StaticFileHandler,dict(path=config.settings['static_path'],default_filename="index.html")),
        # (r'/(.)*', notFoundHandler.NotFoundHandler)
    ]
