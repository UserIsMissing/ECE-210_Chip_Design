`default_nettype none

module lif_ref (
    input wire [7:0]    current,
    input wire          clk,
    input wire          reset_n,
    output reg [7:0]    state,
    output wire         spike
);

    wire [7:0] next_state;
    reg [7:0] threshold;
    reg [3:0] ref_count; // 4-bit counter for refractory period

    // Only spike if not in a refractory period
    assign spike = (state >= threshold) && (ref_count == 0);

    // next state: bit shift-leak
    // if in a refractory period, next state forced to 0
    assign next_state = (ref_count > 0) ? 8'd0 : current + (state >> 1)

    always @(posedge clk) begin
        // reset logic
        if (!reset_n) begin
            state <= 0;
            threshold <= 200;
        end else begin
            state <= next_state;
        end
    end

    // next state logic
    assign next_state = current + (state >> 1);

    // spiking logic
    assign spike = (state >= threshold);

endmodule