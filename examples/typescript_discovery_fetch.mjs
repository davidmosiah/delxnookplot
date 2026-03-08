const urls = [
  'https://api.delx.ai/.well-known/agent-card.json',
  'https://api.delx.ai/.well-known/delx-capabilities.json'
];
for (const url of urls) {
  const res = await fetch(url);
  const data = await res.json();
  console.log(url, Object.keys(data).slice(0,5));
}
