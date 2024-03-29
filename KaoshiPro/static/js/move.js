function getStyleAttr(obj,attr){
	if (window.getComputedStyle){
		return getComputedStyle(obj,null)[attr];
	}
	else {
		return obj.currentStyle[attr];
	}
}



//改变同一个元素的不同属性值
function animate(obj, json, fn){  
	
	clearInterval(obj.timer);
	obj.timer = setInterval(function(){
		
		//表示是否所有属性都到达目标值了
		var bStop = true;
		
		for (var attr in json) {
			var iTarget = json[attr]; //目标值
			
			//1, current
			var current;
			if (attr == "opacity") {  //透明度
				current = Math.round(getStyleAttr(obj, attr) * 100);
			}
			else { //left,top,width,height...
				current = parseFloat(getStyleAttr(obj, attr));  
				current = Math.round(current); //四舍五入
			}
			
			//2, 速度
			var speed = (iTarget-current)/8;
			speed = speed>0 ? Math.ceil(speed) : Math.floor(speed);  
			
			//3, 临界值
			if (current != iTarget) {
				//如果有一个属性没有到达目标值，则不能停止定时器，将bStop=false
				bStop = false;
			}
			
			//4, 运动  
			if (attr == "opacity") {
				obj.style[attr] = (current + speed)/100;
				obj.style.filter = "alpha(opacity="+ (current + speed) +");"
			}
			else {
				obj.style[attr] = current + speed + "px";
			}
		
		}
		
		if (bStop) {
			clearInterval(obj.timer); //停止定时器, 停止运动
			if (fn) fn();			
		}
		
		
	}, 30);

}










//缓冲运动封装
function move(obj, attr, iTarget, fn){  //fn=function(){}
	
	clearInterval(obj.timer);
	obj.timer = setInterval(function(){
		
		//1, current
		var current;
		if (attr == "opacity") {  //透明度
			current = Math.round(getStyleAttr(obj, attr) * 100);
		}
		else { //left,top,width,height...
			current = parseFloat(getStyleAttr(obj, attr));  
			current = Math.round(current); //四舍五入
		}
		
		//2, 速度
		var speed = (iTarget-current)/8;
		speed = speed>0 ? Math.ceil(speed) : Math.floor(speed);  
		
		//3, 临界值
		if (current == iTarget) {
			clearInterval(obj.timer); //停止定时器, 停止运动
			
			//回调
			if (fn) fn();
			
			return;
		}
		
		//4, 运动  
		if (attr == "opacity") {
			obj.style[attr] = (current + speed)/100;
			obj.style.filter = "alpha(opacity="+ (current + speed) +");"
		}
		else {
			obj.style[attr] = current + speed + "px";
		}
		
	}, 30);

}
