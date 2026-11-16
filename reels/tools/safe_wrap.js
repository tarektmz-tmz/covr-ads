// Put at the start of a reel page's main script (after the static containers exist).
// Scales every layer except the background and the avatar to 88% around the centre so it stays inside Instagram's visible area.
(function(){const st=document.getElementById('st');const w=document.createElement('div');w.id='content';
w.style.cssText='position:absolute;inset:0;transform:scale(.88);transform-origin:50% 50%';
[...st.children].forEach(c=>{if(!c.matches('.bg,.bgb,.shade,.vig,#me,#glow'))w.appendChild(c)});
st.insertBefore(w,document.getElementById('me'))})();
