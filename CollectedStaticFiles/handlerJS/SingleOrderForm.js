$(document).ready(
		
		function() {
			$("#SubmitOne").unbind("click").click(
					function() {
						console.log('submit');
						var v = $('#inputDate').datebox('getValue');
						if ('' == v) {
							alert('请输入日期!');
						} else if ("" == $("#mainOrderID").val()){
							alert('请输入主单号!');
						}
						else {
							console.log('new location');
							var newLocation = "/WebUI/mainInputForm?"
									+ "airCompany=" + $("#airCompany").val()
									+ "&mainOrderID=" + encodeURI($("#mainOrderID").val())
									+ "&mainOrderInputDate="
									+ $('#inputDate').datebox('getValue');
							$(window.location).attr("href", newLocation);
						}
					});
		}
		
);