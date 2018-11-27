$(function(argument) {
	let clsid = getQueryVariable('clsid')
	getData(clsid)
})


function getData(clsid) {
	$.get('/api/query_class?clsid='+clsid, function(data) {
		if(data['error'] == 0){
			setData(data['data'])
		}
	});
}

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

function setData(data) {
	let html
	html = template('data',{'data':data})
	$('.main ul').html(html)
	getComInfos();
	setTouch();
}

function getComInfos(argument) {
	$('.main li').click(function(event) {
		let cid = $(this).data('id')
		location.href = '/m.infos.html?cid=' + cid;
	});
}

function setTouch(argument) {
	$('.main li').on('touchstart', function(event) {
		// event.preventDefault();
		$(this).find('.title').removeClass('invisible')
		$(this).find('.price').removeClass('invisible')
	});

	$('.main li').on('touchend', function(event) {
		// event.preventDefault();
		$(this).find('.title').addClass('invisible')
		$(this).find('.price').addClass('invisible')
	});
}