// Components
import EditSummary from "./EditSummary";

// Functions
import { useState } from "react";
import { parseISO, format } from "date-fns";

// Icons
import { MdOutlineEditNote } from 'react-icons/md';

export default function Summary({ summary, totalSpent, isEditingSummary, setIsEditingSummary, onSummaryEdit }) {
    // Guard against slow return of db object
    if(!summary) {
        return <div>Summary loading...</div>;
    }

    // Convert last_updated to mm/dd/yy format
    const last_updatedDateObj = parseISO(summary.last_updated)
    const formattedLastUpdatedDate = format(last_updatedDateObj, 'MM/dd/yy')

    return (
        <div className="summary">
            <div className="summary-budget">
                { isEditingSummary ? (
                    <EditSummary summary={summary} setIsEditingSummary={setIsEditingSummary} onSummaryEdit={onSummaryEdit}/> 
                ) : (
                    <>
                        <div className="summary-budget-header">
                            <h4>Budget</h4>
                            <MdOutlineEditNote onClick={() => setIsEditingSummary(true)}/>
                        </div>
                        <h5>{summary.budget}</h5>
                        <p>Updated: {formattedLastUpdatedDate}</p>
                    </>
                )}
            </div>

            <div className="summary-spent">
                <h4>Spent</h4>
                <h5>${(totalSpent).toFixed(2)}</h5>
            </div>

            <div className="summary-remaining">
                <h4>Remaining</h4>
                <h5>${(summary.budget - totalSpent).toFixed(2)}</h5>
            </div>
        </div>
    );
}