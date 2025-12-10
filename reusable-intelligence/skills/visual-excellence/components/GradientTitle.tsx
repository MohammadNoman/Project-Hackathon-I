import React from 'react';

export const GradientTitle = ({ title, subtitle }: { title: string; subtitle?: string }) => (
    <div className="mb-12 animate-slide-up">
        {subtitle && (
            <span className="block text-brand-400 font-bold tracking-widest uppercase text-sm mb-2">
                {subtitle}
            </span>
        )}
        <h1 className="text-4xl md:text-6xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-brand-600 pb-2">
            {title}
        </h1>
    </div>
);
