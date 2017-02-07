$(document).ready(
		function() {
			var GET = $.urlGet(); //获取URL的Get参数
			var inputDate = GET['mainOrderInputDate']; //取得输入日期
			$('#mainOrderInputDate').datebox('setValue', inputDate);
			var airCompany = decodeURI(GET['airCompany']); //取得航空公司
			$('#airlines').textbox('setValue', airCompany);
			var mainOrderID = decodeURI(GET['mainOrderID']); //取得主单id
			console.log(mainOrderID);
			$('#MAWBNO').textbox('setValue', mainOrderID);
			
			$("#SubmitBtn").unbind("click").click(
					function() {
						console.log('SubmitBtn');
						var dataArray = new Array();
						$(".dataElemMark").each(function(){
							var curData = new Object();
				            var id = $(this).attr("id");
				            var val = $(this).val();
//				            alert(id + "的val=" + val);
				            curData.id=id;
				            curData.val=val;
				            if("" == curData.val){
				            	var classStr = $(this).attr("class");
				            	if(classStr.indexOf("dataElemMarkDate") > 0){
				            		curData.val = $(this).datebox('getValue');
				            	} else if(id == "mainID"){
				            		curData.val = $(this).text();
				            	}
				            }
				            
				            dataArray.push(curData);
						});
						
						var jsonStr = JSON.stringify(dataArray);
//						alert(jsonStr);
						
						$.post("/WebUI/SubmitOrder", jsonStr, function(data, status) {
							if (null == data) {
								alert("返回数据为空");
								return;
							}

							if ("0" == data.errorCode) {
								alert("提交成功");
							} else {
								if ("1" == data.errorCode) {
									alert("只能用post方式哦");
								} else if ("2" == data.errorCode) {
									alert("异常错误");
								} else {
									alert("未知错误");
								}
							}
						})
					});
		}
);
