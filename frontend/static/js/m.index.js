$(function() {
	getRecommendData();
	getComData();
})


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
	// slidesClick();
}

// function slidesClick() {
// 	$('.picSlides').
// }

function getComData() {
	$.get('/api/index_data', function(data) {
		if(data['error'] == 0){
			let comData = []
			for(var i in data['data']){
				for(var x in data['data'][i]){
					comData.push(data['data'][i][x])
				}
			}
			setData(comData)
		}
	});
}

function setData(data) {
	// console.log(data)
	let html
	html = template('data',{'data':data})
	$('.main ul').html(html)
	getComInfos();
}

function getComInfos(argument) {
	$('.main li').click(function(event) {
		let cid = $(this).data('id')
		// console.log(cid)
		location.href = '/m.infos.html?cid=' + cid;
	});
}