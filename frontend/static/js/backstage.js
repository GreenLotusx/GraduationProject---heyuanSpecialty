$(function () {
	check_login();
	getData();
	deleteData();
	queryLike();
})

function check_login(){
	$.ajax({
		url: '/api/check_login',
		type: 'GET',
		dataType: 'json',
	})
	.done(function(data) {
		if (data['error'] == 0){
			if(data['data']['identity'] <= 1){
				let html = data['data']['time'] + "&nbsp;&nbsp;&nbsp;&nbsp;欢迎您&nbsp;&nbsp;&nbsp;&nbsp;<span>"+ data['data']['name'] +"</span>&nbsp;&nbsp;&nbsp;&nbsp;<a href='#' onclick='logout();'>注销</a>"
				$('.wecome').html(html)
			}else{
				location.href = '/login.html';
				// alert('你没有权限访问此页面');
			}
		}else{
			location.href = '/login.html';
		}
	})
	.fail(function() {
		alert('发生异常错误')
	})
}

function deleteData() {
	$('body').on('click','#delete',function(event) {
		let cid = $(this).data('id')
		let tf = del()
		if (tf == true){
			delData(cid)
		}
	});
}

function del() {
// 弹出确认删除的窗口
 var msg = "此操作不可逆!\n确定要删除本条数据吗？"; 
 if (confirm(msg)==true){ 
  return true; 
 }else{ 
  return false; 
 } 
}

function delData(cid) {
	$.get('/api/delete_commodity?cid='+cid, function(data) {
		if(data['error'] == 0){
			// alert(data['data']);
			getData();
		}else{
			alert('商品数据删除失败')
		}

	});
}


function queryLike() {
	$('#queryLikes').click(function(event) {
		event.preventDefault();
		let originalData = $(".operation form").serializeArray();
		$.get('/api/query_like?keyword='+originalData[0]['value'], function(data) {
			if(data['error'] == 0){
				setData(data['data'])
			}
		});
	});
}


function logout() {
	$.get('/api/logout', function(data) {
		if (data['error'] == 0){
			location.href = '/login.html';
		}else if(data['error'] == -5){
			alert('注销失败,请刷新重试')
		}
	});
}



function getData() {
	let page = getQueryVariable('page')
	$.get('/api/many_commodity?page='+ page, function(data) {
		if(data['error'] == 0){
			setData(data['data'])
		}
	});
}

function setData(data) {
	if (data != undefined){
		page_sum = data['page_sum']
		page = data['page']
		if(data['com_data'] == undefined){
			data = data
		}else{
			data = data['com_data']
		}

		data.reverse()
	}	//将数据倒序排序,因为是顺序插入节点
	$('.data_list_body').remove()
	for(var i in data){
		var li1 = "<li><img src="+ data[i]['img'] +"></li>"
		var li2 = "<li>"+ data[i]['title'] +"</li>"
		var li3 = "<li>"+ data[i]['freight']+"</li>"
		var li4 = "<li>"+ data[i]['ordprice']+"</li>"
		var li5 = "<li>"+ data[i]['price']+"</li>"
		var li6 = "<li>"+ data[i]['sales']+"</li>"
		var li7 = "<li>"+ data[i]['specifications']+"</li>"
		var li8 = "<li>"+ data[i]['class']+"</li>"
		var li9 = "<li><a href='changedata.html?cid="+data[i]['id']+"'>编辑</a>&nbsp;&nbsp;| &nbsp;&nbsp;<a href='#' id='delete' data-id='"+data[i]['id']+"'>删除</a></li>"
		var div = "<div class='data_list_body'>"+li1+li2+li3+li4+li5+li6+li7+li8+li9+"</div>"
		$('.data_list_title').after(div)
	}

	var divNum = $('.sub_body').children("div").length
	if ( divNum < 13){
		for (var i = 0; i < 13 - divNum; i++) {
			var li1 = "<li></li>"
			var li2 = "<li></li>"
			var li3 = "<li></li>"
			var li4 = "<li></li>"
			var li5 = "<li></li>"
			var li6 = "<li></li>"
			var li7 = "<li></li>"
			var li8 = "<li></li>"
			var div = "<div class='data_list_body'>"+li1+li2+li3+li4+li5+li6+li7+li8 +"</div>"
			$('.subject .data_list_body').last().after(div)
		}
	}

	if(page <= 1){
		lastpage = 1
		nextpage = page + 1
	}else if(page >= page_sum - 1){
		lastpage = page - 1
		nextpage = page_sum
	}


	$('#head').attr('href', '/backstage.html?page=1');
	$('#last').attr('href', '/backstage.html?page='+lastpage);
	$('#next').attr('href', '/backstage.html?page='+nextpage);
	$('#foot').attr('href', '/backstage.html?page='+page_sum);

}