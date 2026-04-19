async function loadData(symbol) {
    const response = await fetch(`/summary/${symbol}`);
    const data = await response.json();

    document.getElementById("result").innerHTML =
        `
        <h2>${symbol}</h2>
        <p>52 Week High: ₹${data["52_week_high"]}</p>
        <p>52 Week Low: ₹${data["52_week_low"]}</p>
        <p>Average Close: ₹${data["average_close"]}</p>
        `;
}
