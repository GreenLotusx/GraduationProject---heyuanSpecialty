$(function() {
	getData();
	getPage();
	delCartItem();
})


function getPage(argument) {
	$('.payment').click(function(event) {
		let value = "?"
		let num = 0
		$('.commodity li').each(function(index, el) {
			if ($(this).find('.select').prop('checked') == true) {
				num++;
				value = value + 'cid' + num + "=" + $(this).find('.select').val() + "&" + 'num' + num + "=" + $(this).find('.num_show').val() + "&";
			}
		});
		value += "num="+num + "&from=cart"
		location.href = '/place_order.html' + value;
	});
}


function getData() {
	$.get('/api/query_cart', function(data) {
		if(data['error'] == 0){
			setData(data['data'])
		}
	});
}

function setData(data) {
	if(data == undefined){
		let div = "<div style='min-height: 300px;font-size: 25px;line-height: 300px;color:#616A6B;text-align: center;'>购物车空空如也~~</div>"
		$('.commodity ul').html(div)
	}else{
		let html
		html = template('cartList',{'cartList':data})
		$('.commodity ul').html(html)
		numChange();
		// checkBoxSelect();
		checkedChange();
		setSelectNum();
		setMoney();
	}
}

function numChange() {
	let li = $('.commodity li')
	let num
	let num_show
	li.each(function(index, el) {
		var then = $(this)
		$(this).find('.add').click(function(event) {
			num_show = then.find('.num_show')
			num = num_show.val()
			num++;
			num_show.val(num)

			setMoney();
			then.find('.money').text((Number(then.find('.new').text()) * num).toFixed(2))
		});

		$(this).find('.minus').click(function(event) {
			num_show = then.find('.num_show')
			num = num_show.val()
			if (num == 1){
				num = 1;
			}else{
				num--;
			}
			num_show.val(num)
		
			setMoney();
			then.find('.money').text((Number(then.find('.new').text()) * num).toFixed(2));

		});

		$(this).find('.num_show').change(function(event) {
			num = $(this).val()
			if(num >99 ){
				num = 99
				$(this).val(99)
			}else if(num < 1){
				num = 1
				$(this).val(1)
			}
			setMoney();
			then.find('.money').text((Number(then.find('.new').text()) * num).toFixed(2));
		});

	});
}


function checkedChange() {
	$('.select').change(function(event) {
		checkBoxSelect();
		if($(this).prop('checked') == true){
			$(this).prop('checked',true);
		}else{
			$(this).prop('checked',false);
		}
		setSelectNum();
		setMoney();
	});

	$('#allSelect').change(function(event) {
		if($(this).prop('checked') == true){
			$('.select').each(function(index, el) {
				$(this).prop('checked',true);
			});
		}else{
			$('.select').each(function(index, el) {
				$(this).prop('checked',false);
			});
		}
		setSelectNum();
		setMoney();
	});
}

function checkBoxSelect(argument) {
	let len = $('.select').length
	let all = 0
	$('.select').each(function(index, el) {
		if($(this).prop('checked') == false){
			$('#allSelect').prop('checked',false);
		}else{
			all++;
		}
	});
	if(all == len){
		$('#allSelect').prop('checked',true);
	}
}

function setSelectNum() {
	let all = 0
	$('.select').each(function(index, el) {
		if($(this).prop('checked') == true){
			all++;
		}
	});
	$('.selection span').text(all)
}

function setMoney(argument) {
	let li = $('.commodity li')
	var sumMoney = 0
	li.each(function(index, el) {
		if ($(this).find('.select').prop('checked') == true) {
			let num = $(this).find('.num_show').val()
			let price = $(this).find('.new').text()
			let sum = Number(num) * Number(price)
			sumMoney = sumMoney + sum
		}
	});
	sumMoney = sumMoney.toFixed(2)
	$('.moneyTotal span').text('￥'+sumMoney)
}

function delCartItem() {
	$('body').on('click', '.operation a', function(event) {
		let cid = $(this).data('id')
		$.get('/api/delete_cart?cid='+ cid, function(data) {
			if(data['error'] == 0){
				alert(data['data'])
				getData();
			}else{
				alert(data['商品删除失败'])
			}
		});
	});

	$('body').on('click', '.clearCart', function(event) {
		if(del() == true){
			$.get('/api/delete_cart', function(data) {
				if(data['error'] == 0){
					alert("购物车已经全部清空")
					getData();
				}else{
					alert("清空购物车失败")
				}
			});
		}
	});
}


function del() {
// 弹出确认删除的窗口
 var msg = "此操作不可逆!\n确定要清空购物车吗？"; 
 if (confirm(msg)==true){ 
  return true; 
 }else{ 
  return false; 
 } 
}