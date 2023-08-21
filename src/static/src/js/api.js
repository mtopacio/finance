import { _ } from 'lodash';

const apiUrl = "http://localhost:8000"

export async function getInstrument(symbol) {
    
    const url = `${apiUrl}/instrument?symbol=${symbol}`

    return await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
             "Origin": "localhost",
        }
    }).then(resp => {
        return resp.json()
    })
}

export async function getQuote(symbol) {
    const url = `${apiUrl}/quotes?symbol=${symbol}`
    return await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
             "Origin": "localhost",
        }
    }).then(resp => {
        return resp.json()
    })
}

export async function getHistoricals(symbol) {
    const url = `${apiUrl}/historicals?symbol=${symbol}`
    return await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
             "Origin": "localhost",
        }
    }).then(resp => {
        return resp.json()
    }).then(resp => {
        return resp.results[0].historicals
    })
}

export async function getOptions(symbol) {
    const url = `${apiUrl}/options?symbol=${symbol}`
    return await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
             "Origin": "localhost",
        }
    }).then(resp => {
        return resp.json()
    }).then(resp => {
        console.log(resp);
        return {
            calls: _.sortBy(resp.calls.map(r => {
                let tmp = {...r}
                tmp.strike_price = parseFloat(tmp.strike_price);
                return tmp
            }), ['strike_price']),
            puts: _.sortBy(resp.puts.map(r => {
                let tmp = {...r}
                tmp.strike_price = parseFloat(tmp.strike_price);
                return tmp
            }), ['strike_price'])
        };
    })
}

export async function getOption(uuid) {
    const url = `${apiUrl}/option?id=${uuid}`
    return await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
             "Origin": "localhost",
        }
    }).then(resp => {
        return resp.json()
    })
}

export async function getPrice(symbol) {
    const url = `${apiUrl}/price?symbol=${symbol}`
    return await fetch(url, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
             "Origin": "localhost",
        }
    }).then(resp => {
        return resp.json()
    })
}