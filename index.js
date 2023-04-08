const rl = require("readline-sync"),
	axios = require("axios"),
	exs = ["dishcatfish.com", "coffeetimer24.com", "waterisgone.com", "plancetose.com"],
	rand = (arr) => arr[Math.floor(Math.random() * arr.length)],
	sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

axios.defaults.headers.common = {
	"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
	Accept: "*/*",
	"X-Client-ID": "Web",
};

function randomStr(length) {
	let result = "";
	const characters = "abcdefghijklmnopqrstuvwxyz0123456789";
	for (let i = 0; i < length; i++) {
		result += characters.charAt(Math.floor(Math.random() * characters.length));
	}
	return result;
}

(async () => {
	const reff = rl.question("[?] URL Reff: "),
		loop = rl.question("[?] Jumlah Reff: "),
		instance = axios.create();

	const reffUuid = await instance.get(reff).then((res) => res.request.res.responseUrl.match(/(?<=invitedby=)(.*)(?=&)/g)[0]);

	for (let i = 1; i <= loop; i++) {
		let ex = rand(exs),
			uName = randomStr(7),
			mail = `${uName}@${ex}`;

		console.log(`\n[${i}] Create an Account | ${mail}`);

		await axios.post("https://api.internal.temp-mail.io/api/v3/email/new", { domain: ex, name: uName });

		await instance.post("https://user.atlasvpn.com/v1/request/join", {
			email: mail,
			marketing_consent: false,
			referrer_uuid: reffUuid,
			referral_offer: "initial",
		});

		console.log(`[${i}] Wait Email | ${mail}`);
		let auth;
		while (true) {
			var emailData = await axios.get("https://api.internal.temp-mail.io/api/v3/email/" + mail + "/messages").then((res) => res.data);
			if (emailData.length !== 0) {
				auth = emailData[0].body_text.match(/(?<=token=)(.*)(?= \))/g)[0];
				break;
			}
			await sleep(1000);
		}
		instance.defaults.headers.common.Authorization = "Bearer " + auth;

		console.log(`[${i}] Verif Email | ${mail}`);
		let verif = await instance.get("https://user.atlasvpn.com/v1/auth/confirm");
		console.log(`[${i}] ${mail} => Done Registered!`);
	}
})();
