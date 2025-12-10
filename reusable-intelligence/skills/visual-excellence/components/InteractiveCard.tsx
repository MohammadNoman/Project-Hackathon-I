import React from 'react';
import { ChevronRight } from 'lucide-react';

export const InteractiveCard = ({ title, description, onClick }: any) => (
    <div
        onClick={onClick}
        className="group p-6 rounded-xl border border-slate-800 bg-slate-900/50 hover:bg-slate-800/80 hover:border-brand-500/50 transition-all duration-300 cursor-pointer shadow-lg hover:shadow-brand-500/10"
    >
        <div className="flex items-center justify-between">
            <div>
                <h3 className="text-xl font-bold text-slate-100 group-hover:text-brand-300 transition-colors">
                    {title}
                </h3>
                <p className="mt-2 text-slate-400 text-sm leading-relaxed">
                    {description}
                </p>
            </div>
            <ChevronRight className="w-5 h-5 text-slate-600 group-hover:text-brand-400 transform group-hover:translate-x-1 transition-all" />
        </div>
    </div>
);
