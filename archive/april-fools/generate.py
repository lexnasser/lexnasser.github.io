url = "/2023/04/01/google-is-acquiring-stripe/"


with open("src.html", "r") as f:
	contents = f.read()

contents = contents.replace("Fitbit", "Stripe")
contents = contents.replace("fitbit", "stripe")
contents = contents.replace("Just days after it was reported", "Just days after rumors circulated")
contents = contents.replace("wearables", "payments")
contents = contents.replace("7.35", "187.35")
contents = contents.replace("2.1", "72")
contents = contents.replace("13:06", "12:06") # 13:06 is 9:06am eastern; send this at 8:33 am eastern time, so set timestamp to 8:06, which is 12:06
contents = contents.replace("19:06", "18:06")
contents = contents.replace("11:06", "10:06")
contents = contents.replace("Hardware", "Fintech")
contents = contents.replace("48843851852_f9159ff13d_c", "GettyImages-1242296087-e1674758354141")
contents = contents.replace("/2019/11/01/google-is-acquiring-fitbit/", url)
contents = contents.replace("2019-11", "2023-04")
contents = contents.replace("November", "April")
contents = contents.replace("2019", "2022")
contents += """
<script>

	videoElement = document.getElementById("RickVideo");
	videoElement.preload='auto';

	window.onclick = function() {
		document.getElementById("myModal").style.display='none';
		videoElement.play()
		videoElement.style.display='';
		document.getElementById("root").style.display='none';
	}

	videoElement.addEventListener("contextmenu", e => e.preventDefault());

</script>"""

contents = contents.replace("""<body class="">""", f"""
	<div id="myModal" class="modal fade in" tabindex="-1" role="dialog" style="min-height:100%; min-width:100%; background-color: rgba(60, 60, 60, 0.5)">
		<div class="modal-dialog" role="document" style="background-color:white; padding-top: 1em; padding-bottom: 1em; padding-left:1em; padding-right: 3em; border-image:linear-gradient(315deg,#00d301,#36c275 50.5%,#00a562); border-image-slice: 1; border-width: 0.25em;overflow-y: hidden;">
			<div class="modal-content">
				<div class="modal-header">
					<h3 class="modal-title">We use cookies!</h3>
					<h5 class="modal-title">To continue please accept our <a href="#">Cookie Policy</a></h5><br>
				</div>
				<button type="button" style="font-family: aktiv-grotesk,sans-serif; font-weight: bold; cursor: pointer;">Accept</button>
				<button type="button" style="font-family: aktiv-grotesk,sans-serif; font-weight: bold; cursor: pointer;">Reject</button>
			</div>
		</div>
	</div>
	<video src="rick.mp4" id="RickVideo" style="display: none; margin: auto; border-radius: 10px; -webkit-box-shadow: 0px 0px 20px 10px rgb(0 0 0 / 26%); box-shadow: 0px 0px 20px 10px rgb(0 0 0 / 26%); width:100%; height:100%;" preload="auto"></video>
<body class="">""")

from pathlib import Path
Path(".." + url).mkdir(parents=True, exist_ok=True)


with open(".." + url + "index.html", "w") as f:
	f.write(contents)