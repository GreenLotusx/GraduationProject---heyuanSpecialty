
$(function() {
	getComData();
	getRecommendData(); 
	apkDown();
})

function getComData() {
	$.get('/api/index_data', function(data) {
		if(data['error'] == 0){
			setData(data['data'])
		}
	});
}

function getRecommendData() {
	$.get('/api/rec_commodities', function(data) {
		if(data['error'] == 0){
			setRecommendData(data['data'])
		}
	});
}

function setRecommendData(data) {
	let excellentData = data['excellent']
	let hotData = data['hot']
	let htmlSlides
	htmlSlides = template('slides', {"excellentData" : excellentData})
	$('.picSlides').html(htmlSlides);
	slidesPlay();
	let hotHtml
	hotHtml = template('hot',{"hot":hotData})
	$('.hot').html(hotHtml)
}


function setData(data) {
	$('.class_item').each(function(index, el) {
		let id = $(this).data('id')
		setItemData(data[id],$(this))
	});
}

function setItemData(itemData,htmlData) {
	let ul = htmlData.children('.class_item_body').children('ul')
	for(var i in itemData){
		let div1 = "<div class='commodityTitle'>"+itemData[i]['title']+"</div>"
		let img = "<img src='"+itemData[i]['img']+"'>" 
		let div2 = "<div class='commodityPic'>" + img +"</div>"
		let div3 = "<div class='commodityPrice'>￥"+ itemData[i]['price'] +"</div>"
		let li = "<li onclick='infosPage("+ itemData[i]['id'] +")'>" + div1 + div2 + div3 + "</li>"
		ul.append(li)
	}

}

function infosPage(cid) {
	location.href = '/infos.html?cid=' + cid;
}

function apkDown(argument) {
	$('.apkdown').mouseenter(function(event) {
		$('.apkdownimg').removeClass('invisible')
	});
	$('.apkdown').mouseleave(function(event) {
		$('.apkdownimg').addClass('invisible')
	});

}