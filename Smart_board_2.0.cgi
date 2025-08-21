#!/usr/bin/perl -w
use CGI;
print "Content-type: text/html\n\n";
print qq {

 <!DOCTYPE html>
 <HTML>
   <HEAD>
	 <TITLE> Visual Smart Board</TITLE>
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">
		<meta http-equiv="X-UA-Compatible" content="IE=7; IE=9; IE=10;" />
		<link rel="stylesheet" href="http://172.22.97.37/SoftFault/VisualSmartBoard/css/styles.css">
		<link rel="stylesheet" href="https://fonts.googleapis.com/icon?family=Material+Icons">
		<link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.4.2/css/all.css" integrity="sha384-/rXc/GQVaYpyDdyxK+ecHPVYJSN9bmVFBvjA/9eOB+pb3F2w2N6fc5qB9Ew5yIns" crossorigin="anonymous">
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
		<link rel="stylesheet" href="https://cdn.datatables.net/1.10.19/css/dataTables.bootstrap.min.css">
		<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>	
		<script src="https://cdn.datatables.net/1.10.19/js/jquery.dataTables.min.js"></script>
		<script src="https://cdn.datatables.net/1.10.19/js/dataTables.bootstrap.min.js"></script>
		 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap.6.2/dist/css/bootstrap.min.css">
  <script src="https://cdn.jsdelivr.net/npm/jquery.6.3/dist/jquery.slim.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js.16.1/dist/umd/popper.min.js"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap.6.2/dist/js/bootstrap.bundle.min.js"></script>
	<style type="text/css">		
		.container
		{
			text-align:center;ackground-color:  #004d99;width:"100";
			height:"100";border: 1px solid rgba(0,0,0,0.1);	border-radius: 12px;
		}
		.navbar
		{
			top:5px;right:5px;width: 100%;overflow: auto;
		}
		.navbar a
		{
			float: left;padding: 10px;color: white;	text-decoration: none;font-size: 20px;width: 25%;
			text-align: center;	border: 3px solid rgba(0,0,0,0.3);border-radius: 20px;background-color: #336699;
			background-image: radial-gradient(100% 100% at 100% 0, #00cccc 0, #006666 100%);
		}
		.navbar a:hover
		{
			background-color:rgba(0,0,0,0.2);color: Black;transform: translateY(-0.5px);
		}
		.navbar a:focus {
			background-color:rgba(0,0,0,0.2);color: Black;
		}
		.navbar1 a
		{
			float: center;padding: 10px;color: white;	text-decoration: none;font-size: 12px;width: 25%;
			text-align: center;	border: 2px solid rgba(0,0,0,0.3);border-radius: 20px;background-color: #336699;
			background-image: radial-gradient(100% 100% at 100% 0, #00cccc 0, #006666 100%);
		}
		.navbar1 a:hover
		{
			background-color:rgba(0,0,0,0.2);color: Black;transform: translateY(-0.5px);
		}
		.navbar1 a:focus {
			background-color:rgba(0,0,0,0.2);color: Black;
		}
		.d
		{
			margin-bottom: 1px;
		}
		.d label
		{
			display: inline-block;
			width: 200px;
			text-align: right;color:black;font-size: 15px;vertical-align: middle;
		}
		.d input
		{
			height: 30px;
			width: 300px;font-size: 20px;
		}
		img.hover-shadow 
		{
			transition: 0.05s;
		}
		img.hover-shadow:hover 
		{
			box-shadow: rgba(45, 35, 66, .4) 0 4px 8px, rgba(45, 35, 66, .3) 0 7px 13px -3px, #3c4fe0 0 -3px 0 inset;
			transform: translateY(-5px);
		}
		
		.button{
			float: center;padding: 10px;color: black;	text-decoration: none;font-size: 25px;width: 60%;
			text-align: center;	border: 3px solid rgba(0,0,0,0.3);border-radius: 20px;background-color: #ADD8E6;
			background-image: radial-gradient(100% 100% at 100% 0, #ADD8E6 0, #ADD8E6 100%);
		}

.button:focus {
			box-shadow: #3c4fe0 0 0 0 1.5px inset, rgba(45, 35, 66, .4) 0 2px 4px, rgba(45, 35, 66, .3) 0 7px 13px -3px, #3c4fe0 0 -3px 0 inset;color: White;
		}

.button:hover {
			
			transform: translateY(-0.5px);
		}

.button:active {
			box-shadow: #3c4fe0 0 3px 7px inset;
			transform: translateY(2px);
		}
		.btn button
		{
			align:right;padding:2px;color: black;background-image: radial-gradient(100% 100% at 100% 0, #ADD8E6 0, #ADD8E6 100%);background-color:#ADD8E6;text-decoration: none;font-size: 15px;width: 200%
		}
		.btn:focus {
			box-shadow: #3c4fe0 0 0 0 1.5px inset, rgba(45, 35, 66, .4) 0 2px 4px, rgba(45, 35, 66, .3) 0 7px 13px -3px, #3c4fe0 0 -3px 0 inset;color: White;
		}
	</style>
		<!-- Include jQuery and PowerTip -->
	<script type="text/javascript" src="./js/jquery.powertip.js"></script>
	<link rel="stylesheet" type="text/css" href="./css/jquery.powertip.css" />
		<script type="text/vbscript">
		    function GetComputerName()
		    	Dim WshNetwork
		    	Set WshNetwork = CreateObject("WScript.Network")
		    	ComputerName = WshNetwork.ComputerName
		    	
		    	Dim Prefix, PrefixMatch
		    	Prefix = LCase(Left(ComputerName, 3))
		    	
		    	PrefixMatch = (Prefix = "ms-") Or (Prefix = "hs-") Or (Prefix = "cc-")
		    	'msgbox Prefix & "-" & ComputerName
				GetComputerName=ComputerName
		    	If PrefixMatch Then
		    	  msgbox Prefix & "-" & ComputerName
		    	End If
		    End function
			function GetUserCount()
				dim ComputerName
				ComputerName=GetComputerName()
					Dim timeStamp
					timeStamp = Month(Date)&"-"&Day(Date)&"-"&Year(Date)	
					dim tm
					tm = Time()
					timeStamp=timeStamp &","&tm&"," &ComputerName
					'msgbox tm
					GetUserCount=timeStamp
					
			End Function
		</script>
		
		<script type="text/javascript">
			var userN;
			var AppName;
			
			function WriteUserDetails(ApplicationName)
			{
				var dt=GetUserCount();
				AppName=ApplicationName;
				var WinNetwork = new ActiveXObject("WScript.Network");
				//alert(WinNetwork.UserName);
				userN=WinNetwork.UserName;
				//alert(dt);alert("h");
				//alert(AppName);
				CallAjax(dt);
			} 
			function showPreviousWindow() 
			{
				  //alert("Smart");
				  //document.getElementById("clear").href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/Clearance/Clearance.html"; 
				  document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/cgi/SmartBoard_1.cgi"; 
				return false;
			}
			 
			function ShowAppWindow()
			{			
				if(AppName=="Clash Analyzer")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/Clearance/Clash_Analyzer.html";}
				
				else if(AppName=="JT Attribute Compare App")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/App_JtPropertiesCompare/main.html";}
				
				else if(AppName=="DMU Vehicle BOM Report")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/VisualBOMReports/DMU_Vehicle_BOM_Report.html";}
				
				else if(AppName=="Weld Spot Visualizer")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/WeldSpotReport/Weld_Spot_Visualizer.html";}
				
				else if(AppName=="Material Vs Thickness Review")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/VisualSmartAttribute/Material_Vs_Thickness_Smart_Review.html";}
				
				else if(AppName=="Smart DMU Calculator")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/Dynamic_Calculation/Smart_DMU_Calculator.html";}
				
				else if(AppName=="CoG Estimator")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/CG_Calculation/CoG_Estimator.html";}
				
				else if(AppName=="Intelligent DMU Compare")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/JTCompare/BOMCompare.html";}				
				
				else if(AppName=="3D Matrix Extractor")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/Transformation/GetTransformation.html";}
				
				else if(AppName=="One Click 3D Compare")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/3DCompare/geometry_comapare.html";}
				
				else if(AppName=="PCCR")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/App_PCCR/App_PCCR.html";}
				
				else if(AppName=="TML Cost Finder")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/DPDS_SAP_App/html/DPDS_SAPIntegrationApps.html";}
											
				else if(AppName=="Extract OLD Part")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/OLDJTRev_Report/Extract_OLD_Rev_JT.html";}
				
				else if(AppName=="Map TPL App 2.0")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/DPDS_Module_BOM_Structure_Copy/html/DPDS_Module_BOM_Structure.html";}
				
				else if(AppName=="App Teardown")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/App_TDBM/App_TDBM_Test.cgi";}
				
				else if(AppName=="Ergo Analysis Deck")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/App_Autodeck/Ergo_Analysis_Deck.html";}
				
				else if(AppName=="JT Export 2.0")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/App_JTexport/JT_Export_2.html";}
				
				else if(AppName=="JT to STEP Export")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/App_Export_STP/bin/JT_to_STEP_Export.cgi";}
				
				else if(AppName=="Surrounding Part Search")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/App_Surronding_Part_Search/main.html";}

				else if(AppName=="BOM Comparison")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/App_BOMCompare/app_bom_compare.html";}
				
				else if(AppName=="DVLO")
				{document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/VisualUtilities/DVLO/DVLO_PV.html";}
				
				else
				{ document.getElementById(AppName).href="http://172.22.97.37/SoftFault/VisualSmartBoard/cgi/SmartBoard_QA1.cgi"; }				
				return false;
			}
			
			function CallAjax(dt)
			{
				var rand =Math.random();
				jQuery.ajax({
							url:  'generateJT_QA.cgi', 
							async: false,
						type: "GET",
							data:{UserID:userN,Application:AppName,CurrDate:dt,Random:rand},
							contentType:"text/html",
							success: function(data) {
							//alert("data: "+ data);
							
										jQuery('#loading').hide();
										arr=data;
										//alert(arr);
										if (arr.length!=0)
										{
											alert(arr);
											showPreviousWindow();
										}
										else{ShowAppWindow();}
										//var arr1=arr.split(';');
										//alert("arr 0 is: "+arr1[0]);										
							},
							error: function(data){
								alert("In fail    !!!"+data.responseText);
							}
						});
							
			}
			function call(id)
			{
				if(id=="Home")
				{
					document.getElementById('div_AllApps').style.display = "none";
					document.getElementById('div_Contact').style.display = "none";
					document.getElementById('div_Help').style.display = "none";
					document.getElementById('div_Requirment').style.display = "none";
					document.getElementById('div_Issue').style.display = "none";
					document.getElementById('div_Home').style.display = "Block";
				}
				if(id=="All Apps")
				{
					AllAppsOn();
					document.getElementById('div_AllApps').style.left = "0px";
					document.getElementById('div_Home').style.display = "none";
					document.getElementById('div_Contact').style.display = "none";
					document.getElementById('div_Help').style.display = "none";
					document.getElementById('div_Requirment').style.display = "none";
					document.getElementById('div_Issue').style.display = "none";
					document.getElementById('div_AllApps').style.display ="block";
				}
				if(id=="Help")
				{ 
					document.getElementById('div_AllApps').style.display ="none";
					document.getElementById('div_Home').style.display = "none";
					document.getElementById('div_Contact').style.display = "none";
					document.getElementById('div_Requirment').style.display = "none";
					document.getElementById('div_Issue').style.display = "none";
					document.getElementById('div_Help').style.display = "Block";
				}
				if(id=="Contact")
				{
					document.getElementById('div_AllApps').style.display ="none";
					document.getElementById('div_Home').style.display = "none";
					document.getElementById('div_Help').style.display = "none";
					document.getElementById('div_Requirment').style.display = "none";
					document.getElementById('div_Issue').style.display = "none";
					document.getElementById('div_Contact').style.display = "Block";
				}
				if(id=="Requirement")
				{
					document.getElementById('div_Requirment').style.display = "block";
					document.getElementById('div_Issue').style.display = "none";
				}
				if(id=="Issue")
				{
					document.getElementById('div_Requirment').style.display = "none";
				document.getElementById('div_Issue').style.display = "block";
				}
			}
			function LoadHomePage()
			{
				document.getElementById('div_AllApps').style.display = "none";
				document.getElementById('div_Contact').style.display = "none";
				document.getElementById('div_Help').style.display = "none";
				document.getElementById('div_Requirment').style.display = "none";
				document.getElementById('div_Issue').style.display = "none";
				document.getElementById('div_Home').style.display = "Block";
			}
			function AllAppsOn()
			{
				document.getElementById('div_3D Matrix Extractor').style.display="Block";
				document.getElementById('div_Clash Analyzer').style.display="Block";
				document.getElementById('div_CoG Estimator').style.display="Block";
				document.getElementById('div_DMU Vehicle BOM Report').style.display="Block";
				document.getElementById('div_Ergo Analysis Deck').style.display="Block";
				document.getElementById('div_Extract OLD Part').style.display="Block";
				document.getElementById('div_Intelligent DMU Compare').style.display="Block";
				document.getElementById('div_JT Export 2.0').style.display="Block";
				document.getElementById('div_Map TPL App 2.0').style.display="Block";
				document.getElementById('div_Material Vs Thickness Review').style.display="Block";
				document.getElementById('div_Smart DMU Calculator').style.display="Block";
				document.getElementById('div_Surrounding Part Search').style.display="Block";
				document.getElementById('div_TML Cost Finder').style.display="Block";
				document.getElementById('div_Weld Spot Visualizer').style.display="Block";
				document.getElementById('div_One Click 3D Compare').style.display="Block";
				document.getElementById('div_PCCR').style.display="Block";
				document.getElementById('div_App Teardown').style.display="Block";
				document.getElementById('div_JT to STEP Export').style.display="Block";
				document.getElementById('div_BOM Comparison').style.display="Block";
				document.getElementById('div_JT Attribute Compare App').style.display="Block";
				document.getElementById('div_DVLO').style.display="Block";
			}
			function AllAppsOff()
			{
				document.getElementById('div_3D Matrix Extractor').style.display="none";
				document.getElementById('div_Clash Analyzer').style.display="none";
				document.getElementById('div_CoG Estimator').style.display="none";
				document.getElementById('div_DMU Vehicle BOM Report').style.display="none";
				document.getElementById('div_Ergo Analysis Deck').style.display="none";
				document.getElementById('div_Extract OLD Part').style.display="none";
				document.getElementById('div_Intelligent DMU Compare').style.display="none";
				document.getElementById('div_JT Export 2.0').style.display="none";
				document.getElementById('div_Map TPL App 2.0').style.display="none";
				document.getElementById('div_Material Vs Thickness Review').style.display="none";
				document.getElementById('div_Smart DMU Calculator').style.display="none";
				document.getElementById('div_Surrounding Part Search').style.display="none";
				document.getElementById('div_TML Cost Finder').style.display="none";
				document.getElementById('div_Weld Spot Visualizer').style.display="none";
				document.getElementById('div_One Click 3D Compare').style.display="none";
				document.getElementById('div_PCCR').style.display="none";
				document.getElementById('div_App Teardown').style.display="none";
				document.getElementById('div_JT to STEP Export').style.display="none";
				document.getElementById('div_BOM Comparison').style.display="none";
				document.getElementById('div_JT Attribute Compare App').style.display="none";
				document.getElementById('div_DVLO').style.display="none";
			}
			function ShowCategoryApp(category)
			{
				AllAppsOff();
				document.getElementById('div_AllApps').style.left = "1px";
				document.getElementById('div_AllApps').style.display = "Block";
				if(category=="BOM Apps")
				{
					document.getElementById('div_DMU Vehicle BOM Report').style.display = "Block";
					document.getElementById('div_Intelligent DMU Compare').style.display = "Block";
					document.getElementById('div_Map TPL App 2.0').style.display = "Block";
					document.getElementById('div_BOM Comparison').style.display = "Block";
				}
				if(category=="PLM Apps")
				{
					document.getElementById('div_App Teardown').style.display = "Block";
					document.getElementById('div_PCCR').style.display = "Block";
					document.getElementById('div_Extract OLD Part').style.display = "Block";
					document.getElementById('div_TML Cost Finder').style.display="Block";
				}
				if(category=="Export Apps")
				{
					document.getElementById('div_JT Export 2.0').style.display = "Block";
					document.getElementById('div_JT to STEP Export').style.display = "Block";
					document.getElementById('div_Ergo Analysis Deck').style.display="Block";
				}
				if(category=="Analysis Apps") 
				{
					document.getElementById('div_3D Matrix Extractor').style.display = "Block";
					document.getElementById('div_Clash Analyzer').style.display = "Block";
					document.getElementById('div_CoG Estimator').style.display = "Block";				
					document.getElementById('div_Material Vs Thickness Review').style.display = "Block";
					document.getElementById('div_Surrounding Part Search').style.display = "Block";
					document.getElementById('div_Weld Spot Visualizer').style.display = "Block";
					document.getElementById('div_One Click 3D Compare').style.display = "Block";
					document.getElementById('div_Smart DMU Calculator').style.display="Block";
					document.getElementById('div_JT Attribute Compare App').style.display="Block";
					document.getElementById('div_DVLO').style.display="Block";
				}
			}
		</script>
		
   </HEAD>
 <body onload="LoadHomePage()">
  <table style="width: 500%;" class="table table-bordered">
	<div class="MyClass" style="background-color:  #004d99;">			
	<div class="container">
			<div class="image">
				<img class="hover-shadow1" align="center" src="./img/Sanket1.png" width="400" height="100" >
			</div>
				<td id="t1" style="vertical-align:top;height: 50px;text-align:Center;background:#99b3ff;font-weight:bold;color: black;font-size: 37px;font-family:'Fantasy';background-image: radial-gradient(100% 100% at 100% 0, #99b3ff 0, #ff99ff 100%);">VisApp Store v2.0

		<div class="navbar">
			<a onclick="call('Home')" class="active" href="#">Home</a> 
			<a onclick="call('All Apps')" href="#">All Apps</a> 
			<a onclick="call('Contact')" href="#">Contact</a> 
			<a onclick="call('Help')" href="#">Help</a>
		</div>
	</div>
	
	
	    <div id="div_Home"  class="div_Hom" style="border: 5px solid rgba(0,0,0,0.2);right:9px;top:5px;border-radius: 20px;background-color:white;background-image: radial-gradient(100% 100% at 100% 0, #d6d6c2 0, #f5f5f0 100%);">
		
	    	<button class="button" role="button" onclick="ShowCategoryApp('Analysis Apps')">Analytics Apps</button>
	    	<button class="button" role="button" onclick="ShowCategoryApp('Export Apps')">Data Export Apps</button>
	    	<button class="button" role="button" onclick="ShowCategoryApp('BOM Apps')">BOM Apps</button>
	    	<button class="button" role="button" onclick="ShowCategoryApp('PLM Apps')">PLM Apps</button>
	    </div>
		

	<div id="div_Contact" class="container-fluid text-center"  style="border: 5px solid rgba(0,0,0,0.2);right:5px;top:5px;border-radius: 20px;background-color:white;background-image: radial-gradient(100% 100% at 100% 0, #d6d6c2 0, #f5f5f0 100%);">
		<p style="color:green;font-size: 20px;">For any query, Contact with :</p>
		<p style="color:black;font-size: 15px;">sanketas.ttl@ tatamotors.com :</p> 
		<div class="navbar1">
			<a onclick="call('Issue')" href="#">Raise Issue</a> 
			<a onclick="call('Requirement')" href="#">New Requirement</a> 
		</div>
		<div id="div_Requirment">
			<div class="d">
			<label >PV/CV:</label>
			<select name="Type_ID" id = "TypeID" style="font-size: 20px;Height:30px;width:300px;">							
			<option value="PVBU">PVBU</option>
			<option value="CVBU">CVBU</option>
			</select>
			</div>
			<div class="d">
			<label >Department:</label>
			<input type="text" />
			</div>
			<div class="d">
			<label >CAD Number:</label>
			<input type="text" />
			</div>
			<div class="d">
			<label >Requirment:</label>
			<input type="text" /> 
			</div>
			<div class="btn">
	    	<button class="button" role="button" onclick="ShowCategoryApp('Analysis Apps')">Submit</button>
			</div>
		</div> 
		<div id="div_Issue">
			<div class="d">
			<label >Application Name:</label>
			<select name="Type_ID" id = "TypeID" style="font-size: 20px;Height:30px;width:300px;">							
			<option value="PVBU">BOM Compare App</option>
			<option value="CVBU">MAP-TPL App</option>
			</select>
			</div>
			<div class="d">
			<label >PV/CV:</label>
			<select name="Type_ID" id = "TypeID" style="font-size: 20px;Height:30px;width:300px;">							
			<option value="PVBU">PVBU</option>
			<option value="CVBU">CVBU</option>
			</select>
			</div>
			<div class="d">
			<label >Department:</label>
			<input type="text" />
			</div>
			<div class="d"> 
			<label >CAD Number:</label>
			<input type="text" />
			</div>
			<div class="d">
			<label >Issue Description:</label>
			<input type="text" />
			</div>
			<div class="btn">
	    	<button class="button" role="button" onclick="ShowCategoryApp('Analysis Apps')">Submit</button>
			</div>
		</div> 
	</div>
	
	<div id="div_Help" class="container-fluid text-center"  style="border: 5px solid rgba(0,0,0,0.2);right:5px;top:5px;border-radius: 20px;background-color:white;background-image: radial-gradient(100% 100% at 100% 0, #d6d6c2 0, #f5f5f0 100%);">
		<p style="color:green;font-size: 20px;">Download and Save VisApp Store Configuration :</p>
		<a href="Digital_Vehicle_Platform.7z" download> 
		<img class="hover-shadow" align="center" src="./img/download1.png" width="400" height="90" style="width:90px;border-radius: 30%;"></img></a>
		<p style="color:#FFD700;font-size: 20px;text-align:left;">What's New :</p>
	</div>

		
		 
		
		
		 
	<div id="div_AllApps" class="container-fluid text-center"  style="border: 5px solid rgba(0,0,0,0.2);right:5px;top:5px;border-radius: 20px;background-color:#ebebe0;background-image: radial-gradient(100% 100% at 100% 0, #ffe6ff 0, #e6f2ff 100%);">  		
	<div class="row ">
		<div id="div_Clash Analyzer" title="Check Clearnace Between Two JT"  class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	 
			<div class="box" >
				<div class="row">
						<div class="txt-aln-center" >
							<A  AppName="Clash Analyzer" id="Clash Analyzer" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/Clash1.png" width="400" height="90" style="width:90px;border-radius: 30%;">
								<span class="theme-clr"><h5><strong class="momo-font">Clash Analyzer</strong> </h5></span>
							 </A> 							
						</div>	
				</div>											
			</div> 
		</div>
		<div id="div_JT Attribute Compare App" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	  
			<div class="box">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="JT Attribute Compare App" id="JT Attribute Compare App" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
							<img class="hover-shadow" align="center" src="./img/compare1.png" width="400" height="90" style="width:90px;border-radius: 40%;">
							<span class="theme-clr"><h5><strong class="momo-font">JT Attribute Compare App</strong> </h5></span>
							</A>
						</div>	
				</div>										
			</div>		
		</div>
		<div id="div_DMU Vehicle BOM Report" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	  
			<div class="box">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="DMU Vehicle BOM Report" id="DMU Vehicle BOM Report" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
							<img class="hover-shadow" align="center" src="./img/bom2.png" width="400" height="90" style="width:90px;border-radius: 40%;">
							<span class="theme-clr"><h5><strong class="momo-font">DMU Vehicle BOM Report</strong> </h5></span>
							</A>
						</div>	
				</div>										
			</div>		
		</div>
		<div id="div_Weld Spot Visualizer"  class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">		  
			<div class="box">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="Weld Spot Visualizer" id="Weld Spot Visualizer" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
							<img class="hover-shadow" align="center" src="./img/weld.png" width="400" height="90" style="width:90px;border-radius: 30%;">
							<span class="theme-clr"><h5><strong class="momo-font">Weld Spot Visualizer</strong> </h5></span>
							</A>
						</div>	
					</div>											
				</div>
			</div>	
		</div>
		<div id="div_Smart DMU Calculator" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	  
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="Smart DMU Calculator" id="Smart DMU Calculator" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
							<img class="hover-shadow" align="center" src="./img/calculator3.png" width="400" height="90" style="width:90px;border-radius: 30%;">
							<span class="theme-clr"><h5><strong class="momo-font">Smart DMU Calculator</strong> </h5></span>
						</div>	
				</div>										
			</div>	
		</div>	
		<div id="div_CoG Estimator" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	  
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="CoG Estimator" id="CoG Estimator" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/cg.png" width="400" height="90" style="width:90px;border-radius: 30%;">
								<span class="theme-clr"><h5><strong class="momo-font">CoG Estimator</strong> </h5></span>
							 </A> 							
						</div>	
				</div>											
			</div>	
		</div>
		<div id="div_3D Matrix Extractor" title="Get/Set 3D Transformation Matrix values" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	  
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="3D Matrix Extractor" id="3D Matrix Extractor" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/matrix4.png" width="400" height="90" style="width:90px;border-radius: 45%;">
								<span class="theme-clr"><h5><strong class="momo-font">3D Matrix Extractor</strong> </h5></span>
							 </A> 							
						</div>	
				</div>											
			</div>		
		</div>
		<div id="div_One Click 3D Compare" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	  
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="One Click 3D Compare" id="One Click 3D Compare" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/compare1.png" width="400" height="90" style="width:90px;border-radius: 45%;">
								<span class="theme-clr"><h5><strong class="momo-font">One Click 3D Compare</strong> </h5></span>
							 </A> 							
						</div>	
				</div>											
			</div>
		</div>
		<div id="div_PCCR" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="PCCR" id="PCCR" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/nearbypart.png" width="400" height="90" style="width:90px;border-radius: 30%;">
								<span class="theme-clr"><h5><strong class="momo-font">PCCR</strong> </h5></span>
							 </A> 							
						</div>	
				</div>											
			</div>
		</div>
		<div id="div_TML Cost Finder" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="TML Cost Finder" id="TML Cost Finder" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/cost.png" width="400" height="90" style="width:90px;border-radius: 45%;">
								<span class="theme-clr"><h5><strong class="momo-font">TML Cost Finder</strong> </h5></span>
							 </A> 							
						</div>	
				</div>											
			</div>
		</div>	
		<div id="div_Extract OLD Part" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	 
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="Extract OLD Part" id="Extract OLD Part" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/extract.png" width="400" height="90" style="width:90px;border-radius: 45%;">
								<span class="theme-clr"><h5><strong class="momo-font">Extract OLD Part</strong> </h5></span>
							 </A> 							
						</div>	
				</div>										
			</div>
		</div>
		<div id="div_Map TPL App 2.0" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="Map TPL App 2.0" id="Map TPL App 2.0" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/report.png" width="400" height="90" style="width:90px;border-radius: 30%;">
								<span class="theme-clr"><h5><strong class="momo-font">Map TPL App 2.0</strong> </h5></span>
							 </A> 							
						</div>	
				</div>										
			</div>
		</div>
		<div id="div_App Teardown" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	 
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="App Teardown" id="App Teardown" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
							<img class="hover-shadow" align="center" src="./img/teardown1.png" width="400" height="90" style="width:90px;border-radius: 45%;">
							<span class="theme-clr"><h5><strong class="momo-font">App Teardown</strong> </h5></span>
							 </A> 							
						</div>	
				</div>										
			</div>			
		</div>		
		<div id="div_Ergo Analysis Deck" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">					
			<div class="card-body">
				<div class="row">
					<div class="txt-aln-center" >
						 <A AppName="Ergo Analysis Deck" id="Ergo Analysis Deck" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
						 <img class="hover-shadow" align="center" src="./img/otov.png" width="400" height="90" style="width:90px;border-radius: 30%;">
						 <span class="theme-clr"><h5><strong class="momo-font">Ergo Analysis Deck</strong> </h5></span>
						 </A> 							
					</div>												
				</div>
			</div>			
		</div>
		<div id="div_JT Export 2.0" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">				
			<div class="card-body">
				<div class="row">
					<div class="txt-aln-center" >
						<A AppName="JT Export 2.0" id="JT Export 2.0" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
					      <img class="hover-shadow" align="center" src="./img/copy.png" width="400" height="90" style="width:90px;border-radius: 30%;">
							<span class="theme-clr"><h5><strong class="momo-font">JT Export 2.0</strong> </h5></span>
						 </A> 							
					</div>												
				</div>
			</div>			
		</div>
		<div id="div_JT to STEP Export" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	 
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="JT to STEP Export" id="JT to STEP Export" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/export1.png" width="400" height="90" style="width:90px;border-radius: 30%;">
								<span class="theme-clr"><h5><strong class="momo-font">JT to STEP Export</strong> </h5></span>
							 </A> 							
						</div>	
				</div>										
			</div>	
		</div>			
		<div id="div_Surrounding Part Search" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	 
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="Surrounding Part Search" id="Surrounding Part Search" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/pccr.png" width="400" height="90" style="width:90px;border-radius: 40%;">
								<span class="theme-clr"><h5><strong class="momo-font">Surrounding Part Search</strong> </h5></span>
							 </A> 							
						</div>	
				</div>										
			</div>	
		</div>
		<div id="div_BOM Comparison" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	  
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="BOM Comparison" id="BOM Comparison" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/bomcompare.png" width="400" height="90" style="width:90px;border-radius: 30%;">
								<span class="theme-clr"><h5><strong class="momo-font">BOM Comparison</strong> </h5></span>
							 </A> 							
						</div>	
				</div>											
			</div>		 
		</div>
		<div id="div_Intelligent DMU Compare" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	  
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="Intelligent DMU Compare" id="Intelligent DMU Compare" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/compare2.png" width="400" height="90" style="width:90px;border-radius: 30%;">
								<span class="theme-clr"><h5><strong class="momo-font">Intelligent DMU Compare</strong> </h5></span>
							 </A> 							
						</div>	
				</div>											
			</div>		
		</div>
		<div id="div_DVLO" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">	  
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="DVLO" id="DVLO" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
								<img class="hover-shadow" align="center" src="./img/DVLORule.png" width="400" height="90" style="width:90px;border-radius: 30%;">
								<span class="theme-clr"><h5><strong class="momo-font">DVLO</strong> </h5></span>
							 </A> 							
						</div>	
				</div>											
			</div>		
		</div>
		<div id="div_Material Vs Thickness Review" class="col-xl-3 col-lg-3 col-md-3 col-sm-3 col-xs-3 def-col-wdth grid-margin stretch-card mt20">		  
			<div class="card-body">
				<div class="row">
						<div class="txt-aln-center" >
							<A AppName="Material Vs Thickness Review" id="Material Vs Thickness Review" onclick=WriteUserDetails(this.getAttribute('AppName')) HREF="#">
							<img class="hover-shadow" align="center" src="./img/thickness.png" width="400" height="90" style="width:90px;border-radius: 30%;">
							<span class="theme-clr"><h5><strong class="momo-font">Material Vs Thickness Review</strong> </h5></span>
							</A>
						</div>	
				</div>											
			</div>	
		</div>
	</div>		 
	</div>
	</div>
	</table>
</body>
</html>
};