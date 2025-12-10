import { app } from "../../scripts/app.js";

const HEAD_PROMPT_OPTIONS = {
    wear: ["hat", "helmet", "band", "crown", "cap", "hood"],
    color: ["red", "blue", "yellow", "green", "black", "white", "gold", "silver"],
    above: ["Angel ring", "Star", "Clouds", "Halo", "Moon", "Sun"],
    behind: ["tails", "wings", "collars", "cape", "backpack", "aura"],
};

function clampIndex(index, length) {
    return (index + length) % length;
}

function updateWidgetValue(node, widget, value) {
    widget.value = value;
    if (!node.widgets_values) {
        node.widgets_values = node.widgets?.map((w) => w.value ?? null) ?? [];
    }

    const widgetIndex = node.widgets.indexOf(widget);
    if (widgetIndex !== -1) {
        node.widgets_values[widgetIndex] = value;
    }
    node.setDirtyCanvas(true, true);
}

function applyCarousel(widget, node, label) {
    widget.type = "head-prompt-carousel";
    widget.label = label;
    widget.serializeValue = () => widget.value;
    widget.computeSize = () => [node.size[0], 32];
    widget.last_y = 0;
    widget.last_width = node.size[0];
    widget.last_height = 32;

    widget.draw = function (ctx, node, widgetWidth, y) {
        const height = 28;
        this.last_y = y;
        this.last_width = widgetWidth;
        this.last_height = height;
        const padding = 6;
        const buttonWidth = 20;

        ctx.save();
        ctx.fillStyle = "#333";
        ctx.font = "16px sans-serif";

        ctx.fillStyle = "#ddd";
        ctx.textAlign = "left";
        ctx.fillText(label, padding, y + height / 2 + 5);

        const leftX = widgetWidth - (buttonWidth * 2 + padding * 2 + 60);
        const rightX = widgetWidth - (buttonWidth + padding);
        const centerY = y + height / 2;

        ctx.fillStyle = "#555";
        ctx.fillRect(leftX, y + 6, buttonWidth, height - 12);
        ctx.fillRect(rightX, y + 6, buttonWidth, height - 12);

        ctx.fillStyle = "#fff";
        ctx.textAlign = "center";
        ctx.fillText("<", leftX + buttonWidth / 2, centerY + 5);
        ctx.fillText(">", rightX + buttonWidth / 2, centerY + 5);

        ctx.textAlign = "left";
        const valueX = leftX + buttonWidth + padding;
        ctx.fillStyle = "#ddd";
        ctx.fillText(widget.value, valueX, centerY + 5);

        ctx.restore();
    };

    widget.mouse = function (event, pos) {
        if (event.type !== LiteGraph.pointerevents_down) return;
        const [x, y] = pos;
        const height = this.last_height;
        const padding = 6;
        const buttonWidth = 20;
        const leftX = this.last_width - (buttonWidth * 2 + padding * 2 + 60);
        const rightX = this.last_width - (buttonWidth + padding);

        if (y < this.last_y || y > this.last_y + height) return;

        const options = widget.options ?? [];
        if (!options.length) return;
        const currentIndex = options.indexOf(widget.value);
        if (x >= leftX && x <= leftX + buttonWidth) {
            const next = clampIndex(currentIndex - 1, options.length);
            updateWidgetValue(node, widget, options[next]);
            return true;
        }
        if (x >= rightX && x <= rightX + buttonWidth) {
            const next = clampIndex(currentIndex + 1, options.length);
            updateWidgetValue(node, widget, options[next]);
            return true;
        }
    };
}

function setupCarouselWidgets(node) {
    const widgets = node.widgets || [];
    const knownValues = node.widgets_values || [];

    if (!node.widgets_values && widgets.length) {
        node.widgets_values = widgets.map((w) => w.value ?? null);
    }

    Object.entries(HEAD_PROMPT_OPTIONS).forEach(([name, options]) => {
        const widget = widgets.find((w) => w.name === name);
        if (!widget) return;
        if (widget.value === undefined || !options.includes(widget.value)) {
            const savedIndex = widgets.indexOf(widget);
            const savedValue = knownValues[savedIndex];
            widget.value = options.includes(savedValue) ? savedValue : options[0];
        }
        widget.options = options;
        applyCarousel(widget, node, name.charAt(0).toUpperCase() + name.slice(1));
    });
}

app.registerExtension({
    name: "custom.head_prompt.carousel",
    nodeCreated(node) {
        if (node.comfyClass === "HeadPromptNode") {
            setupCarouselWidgets(node);
        }
    },
});
