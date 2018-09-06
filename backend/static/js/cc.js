//Global functions: Captcha Fresh, Modal Alert & Logout
function modalAlert(alertMsg, func) {
	$("nav").after(
	'<div class="modal fade" id="alertModal" tabindex="-1">' +
		'<div class="modal-dialog">' +
			'<div class="modal-content">' +
				'<div class="modal-header">' +
					'<button type="button" class="close" data-dismiss="modal">' +
						'<span aria-hidden="true">&times;</span>' +
					'</button>' +
					'<h5 class="modal-title text-center">系统提示</h5>' +
				'</div>' +

				'<div class="modal-body text-center">' +
					'<h4>' + alertMsg + '</h4>' +
				'</div>' +

				'<div class="modal-footer">' +
					'<button type="button" class="btn btn-primary center-block" data-dismiss="modal">我知道了</button>' +
				'</div>' +
			'</div>' +
		'</div>' +
	'</div>');

	$("#alertModal").modal();
	if (typeof func === 'function') {
		$('#alertModal').on('hide.bs.modal', function () { func(); });
	}
}

//Code for 5 Pages: Load or Send Data
function registerPrepare() {
	$(document).ready(function() {
		applyFormFilled = false;
		$("#register").submit(function(e) {
			e.preventDefault();
			$.post("/api/cc", {
				schoolID: register.stuid.value,
				name: register.name.value,
				sex: register.gender.value == 1 ? "male" : "female",
				dorm: register.dorm.value,
				class: register.class.value,
				telephone: register.tel.value,
				QQnumber: register.QQnumber.value,
				leader: register.leader.value == 1 ? "Yes" : "No",
				email: register.email.value,
				introduce: register.intro.value
			}, function(data){
				if(typeof data === 'string')
					var d = JSON.parse(data);
				else d = data;
				/*if(d.msg === "success") {
					modalAlert(
						'信息提交成功！<br><br>'   
						, function () {
						// freshCaptcha();
						window.location.href = '..';
						});
					}///////////////////////////////////////////////////////////////////////////////////////////
					else {
						modalAlert(d.msg);
						// freshCaptcha();
					}*/
				modalAlert(d.msg);
			});
		});
	});
}
