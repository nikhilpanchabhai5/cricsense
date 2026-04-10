// frontend/js/api.js
const API_BASE = 'http://localhost:5000/api';

async function predictMatch(data) {
    try {
        const response = await fetch(`${API_BASE}/predict`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(data)
        });
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
    }
}

async function getTeams() {
    try {
        const response = await fetch(`${API_BASE}/teams`);
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
    }
}

async function getTeamStats(team) {
    try {
        const response = await fetch(`${API_BASE}/stats/${team}`);
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
    }
}