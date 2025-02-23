"use client";

import { BarChart, Bar, XAxis, YAxis, CartesianGrid, ResponsiveContainer } from "recharts";

const data = [
  { name: "", value: 30 }, // Example value
];

interface PauseBarProps {
  numPauses: number;
};

interface ArticulationBarProps {
  articulationRate: number;
};

export const PauseBar = ({ numPauses } : PauseBarProps) => {
  let barColor = "#eb4444"; // Bad
  
  if (numPauses < 25) {
    barColor = "#22c55e";  // Good
  } else if (numPauses >= 25 && numPauses <= 35) {
    barColor = "#eab308";  // OK
  }  
  return (
    <div className="flex flex-col gap-3 text-sm p-4 rounded-2xl bg-slate-50">
      <p className="font-medium my-auto text-xl">
        Number of Pauses
      </p>
      {/* <div className="flex gap-2 align-middle"> */}
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={[{ name: '', value: numPauses }]}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis domain={[0, 50]} />

          <Bar dataKey="value" fill={barColor} />
        </BarChart>
      </ResponsiveContainer>
      {/* </div> */}
      <div className="font-medium ">
        <span className="font-normal">The interviewee paused {numPauses} times. Any 1+ second gap between speaking counts as a pause.</span>
      </div>
    </div>
  );
};

export const ArticulationBar = ({ articulationRate } : ArticulationBarProps) => {
  let barColor = "#eb4444"; // Bad
  
  if (articulationRate <= 2) {
    barColor = "#eab308";  // OK
  } else if (articulationRate <= 4) {
    barColor = "#22c55e";  // Good
  }  
  return (
    <div className="flex flex-col gap-3 text-sm p-4 rounded-2xl bg-slate-50">
      <p className="font-medium my-auto text-xl">
        Articulation Rate
      </p>
      {/* <div className="flex gap-2 align-middle"> */}
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={[{ name: '', value: articulationRate }]}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis domain={[0, 50]} />

          <Bar dataKey="value" fill={barColor} />
        </BarChart>
      </ResponsiveContainer>
      {/* </div> */}
      <div className="font-medium ">
        <span className="font-normal">The interviewee had an articulation rate of {articulationRate}. Articulation rate expresses talking speed during the interviewee's answers.</span>
      </div>
    </div>
  );
};
