// $(function(){
function slidesPlay() {
	

	var $li = $('.picSlides li');
	var len = $li.length;
	var nowli = 0;
	var prevli = 0;
	var $previous = $('.previous');
	var $next = $('.next');



	$li.not(':first').css({left:800});

	// 通过判断有几张图片就新建几个li标签，作为幻灯片下面的圆点
	$li.each(function(index) {
		var $sli = $('<li>');
		if (index == 0){
			$sli.addClass('active');
		}
		$sli.appendTo('.circle');
	});

	// 幻灯片下面的圆点的点击事件
	$points = $('.circle li');
	$points.click(function(event) {
		nowli = $(this).index();

		if (nowli == prevli) {
			return;
		}
		move();

		$(this).addClass('active').siblings().removeClass('active');

	});



	// 上一页按钮点击事件
	$previous.click(function(event) {
		nowli--;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	});


	// 下一页按钮的点击事件
	$next.click(function(event) {
		nowli++;
		move();
		$points.eq(nowli).addClass('active').siblings().removeClass('active');
	});


	//通过鼠标移入移出事件来选择是否开启计时器，进行循环播放幻灯片
	$('.tempWrap').hover(function() {
		clearInterval(timer)
	}, function() {
		timer = setInterval(autoplay,3500);
	});


	timer = setInterval(autoplay,3500);

// 自动播放函数
function autoplay(){
	nowli++;
	move();
	$points.eq(nowli).addClass('active').siblings().removeClass('active');
}

// 移动图片，实现幻灯片效果
function move(){
	if (nowli < 0){
		nowli = len-1;
		prevli = 0;
		$li.eq(nowli).css({left:-800});
		$li.eq(prevli).stop().animate({left:800},300);
		$li.eq(nowli).stop().animate({left:0},300);
		prevli = nowli;
		return;
	}

	if (nowli > len-1) {
		nowli = 0;
		prevli = len-1;
		$li.eq(nowli).css({left:800});
		$li.eq(prevli).stop().animate({left:-800},300);
		$li.eq(nowli).stop().animate({left:0},300);
		prevli = nowli;
		return;
	}


	if (nowli > prevli){
		$li.eq(nowli).css({left:800});

		$li.eq(prevli).stop().animate({left:-800},300);
	}else{

		$li.eq(nowli).css({left:-800});

		$li.eq(prevli).stop().animate({left:800},300);

	}

		$li.eq(nowli).stop().animate({left:0},300);

		prevli = nowli;
}


// })
}
