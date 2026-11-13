% ============================================================
%  Vacuum Cleaner Robot - 3 Rooms (A, B, C)
%  Robot starts in room A, all rooms are initially dirty.
%
%  Rules:
%   - The robot moves only to ADJACENT rooms.
%   - Exact layout is not fixed: every room is reachable from
%     every other room (change the facts below if the real
%     layout is known). The planner SEARCHES all possibilities,
%     no fixed A-B-C order is hardcoded.
%   - The robot NEVER goes back to room A after leaving it.
%
%  Goal: all three rooms clean (robot may end in any room).
% ============================================================

% --- Adjacency: all rooms mutually reachable ---
adjacent(a, b).
adjacent(b, a).
adjacent(a, c).
adjacent(c, a).
adjacent(b, c).
adjacent(c, b).

% state(RobotPosition, DirtyRooms)
initial(state(a, [a, b, c])).   % start: robot in A, all dirty
goal(state(_, [])).             % goal: no dirty rooms left

% clean(R): clean the room the robot is currently in
move(state(R, Dirty), clean(R), state(R, Rest)) :-
    select(R, Dirty, Rest).

% go(R, To): move to an adjacent room, but NEVER back to room a
move(state(R, Dirty), go(R, To), state(To, Dirty)) :-
    adjacent(R, To),
    \+ (To == a, R \== a).

% --- Planner: depth-first search, never repeats a state ---
% The cut (!) stops the plan as soon as the goal state is
% reached, so no redundant moves are added after cleaning.
solve(State, _, []) :-
    goal(State), !.
solve(State, Visited, [Action | Actions]) :-
    move(State, Action, NextState),
    \+ member(NextState, Visited),
    solve(NextState, [NextState | Visited], Actions).

% --- First plan only ---
start :-
    initial(Init),
    solve(Init, [Init], Plan),
    write('Initial: robot in a, dirty = [a,b,c]'), nl,
    write('Plan:'), nl,
    print_plan(Plan),
    write('Goal reached: all rooms clean!'), nl.

% --- ALL possible plans (every combination) ---
all_plans :-
    initial(Init),
    findall(Plan, solve(Init, [Init], Plan), Plans),
    length(Plans, N),
    write('Total plans found: '), write(N), nl, nl,
    print_all(Plans, 1).

print_all([], _).
print_all([P | Rest], N) :-
    write('--- Plan '), write(N), write(' ---'), nl,
    print_plan(P), nl,
    N1 is N + 1,
    print_all(Rest, N1).

print_plan([]).
print_plan([A | Rest]) :-
    write('  - '), write(A), nl,
    print_plan(Rest).
