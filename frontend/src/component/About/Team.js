import React from "react";


const Team = () => {
  return (
    <div className="Team mt-16">
      <h1 className="text-center font-semibold text-3xl mb-5">Our Team</h1>
      <div className="flex justify-evenly">
        <Member
          name="Kevin Nadar"
          img="kevin-transperent.png"
          title="FastAPI, DBA"
        />
        <Member
          name="Ajaykumar Nadar"
          img="ajaykumar-transperent.png"
          title="React, UI/UX"
        />
        <Member
          name="Vishal Mahajan"
          img="kevin-transperent.png"
          title="FastAPI, ML"
        />
      </div>
    </div>
  );
};
const Member = ({ name, img, title }) => {
  return (
    <div className="Member w-[30%] flex flex-col items-center">
      <div className="w-72 bg-gradient-to-b from-green-400 to-orange-400/30 h-72 px-2 pt-4 rounded-full overflow-hidden">
        <img src={img} alt={name} />
      </div>
      <div className="text-left border-l-[2px] border-solid border-red-500 rounded-sm pl-2">
        <h1 className="font-semibold text-xl">{name}</h1>
        <h2 className="font-semibold text-lg text-gray-500/80">{title}</h2>
      </div>
    </div>
  );
};

export default Team;
