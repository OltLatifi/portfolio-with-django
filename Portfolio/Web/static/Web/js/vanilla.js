

const title = document.querySelector('.anim');
const strTitle = title.textContent;
const splText = strTitle.split('');

title.textContent = '';

for (var i = 0; i < splText.length; i++) {
	title.innerHTML += "<span>" + splText[i] + "</span>";
}

let index = 0;
let timer = setInterval(onTick, 50);

function onTick() {
	const span1 = title.querySelectorAll('span')[index];
	span1.classList.add('fade');
	index++;

	if (index >= splText.length) {
		clearInterval(timer);
		timer = null;
		return;
	}

}
