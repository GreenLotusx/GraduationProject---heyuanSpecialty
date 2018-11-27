$(function(argument) {
	let cid = getQueryVariable('cid');
	getCommodityData(cid)
	// buy()
})


//获取url传入参数
function getQueryVariable(variable)
{
       var query = window.location.search.substring(1);
       var vars = query.split("&");
       for (var i=0;i<vars.length;i++) {
               var pair = vars[i].split("=");
               if(pair[0] == variable){return pair[1];}
       }
       return(false);
}

function getCommodityData(cid) {
	$.get('/api/commodity_data?cid='+cid, function(data) {
		if (data['error'] == 0){
			setData(data['data'])
		}
	});
}

function setData(data) {
	let html
	html = template('infos',{'data':data})
	$('.container').append(html)
}

function buy(argument) {
		alert('手机端没有提供购买功能！请使用PC端进行购买')
}