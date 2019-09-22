var sojaeji = function(sido, gugun, dong) {
	var obj = this;
	//window.onload = function() {
		obj.sido = document.getElementById(sido);
		obj.gugun = document.getElementById(gugun);
		obj.dong = document.getElementById(dong);
		obj.update_sido();
		obj.sido.onchange = function() {
			obj.update_gugun.apply(obj);
			obj.update_dong.apply(obj);
		}
		obj.gugun.onchange = function() {
			obj.update_dong.apply(obj);
		}
	//}
}

sojaeji.prototype = {
	update_gugun : function() {
		if (this.gugun == null) return;
		var gugun = this[this.sido.value];
		this.gugun.innerHTML = "";
		for(var i=0; i<gugun.length; i++)
			this.gugun.options.add(new Option(gugun[i], gugun[i]));
	},
	update_dong : function() {
		if (this.dong == null) return;
		var dong = this[this.sido.value+"->"+this.gugun.value];
		this.dong.innerHTML = "";
		for(var i=0; i<dong.length; i++)
			this.dong.options.add(new Option(dong[i], dong[i]));
	},
	update_sido : function() {
		if (this.sido == null) return;
		var sido = this['½Ãµµ'];
		for(var i=0; i<sido.length; i++)
			this.sido.options.add(new Option(sido[i], sido[i]));
		this.update_gugun();
		this.update_dong();
	}