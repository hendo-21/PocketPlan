import { useState } from "react";

export default function Summary({ summary, totalSpent }) {
    // Guard against slow return of db object
    if(!summary || totalSpent === 0.0) {
        return <div>Summary loading...</div>;
    }

    
    // Prepare state
    const [budget, setBudget] = useState(summary.budget)
    const [last_updated, setLastUpdated] = useState(summary.last_updated)

    return (
        <div className="summary">
            <div className="summary-budget">
                <h4>Budget</h4>
                <p>{budget}</p>
                <p>Last updated: {last_updated}</p>
            </div>

            <div className="summary-spent">
                <h4>Spent</h4>
                <p>${totalSpent}</p>
            </div>

            <div className="summary-remaining">
                <h4>Remaining</h4>
                <p>TODO</p>
            </div>
        </div>
    );
}