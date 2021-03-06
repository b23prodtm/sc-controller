/**
 * SC-Controller - Macro
 *
 * Macro is not registered through keyword, but generated by parser when colon
 * found.
 */
#include "scc/utils/strbuilder.h"
#include "scc/utils/iterable.h"
#include "scc/utils/assert.h"
#include "scc/utils/list.h"
#include "scc/utils/rc.h"
#include "scc/action.h"
#include "macros.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

const char* KW_MACRO = "macro";	// not used normally

typedef struct {
	Action			action;
	ActionList		children;
	int				active;		// -1 for "not active" or index of last executed action
	bool			press;		// If true, next on the "execution plan" is pressing
	bool			repeat;
} Macro;


char* actions_to_string(ActionList l, const char* separator) {
	StrBuilder* sb = strbuilder_new();
	ListIterator it = iter_get(l);
	if ((sb == NULL) || (it == NULL))
		goto actions_to_string_fail;
	if (!strbuilder_add_all(sb, it, &scc_action_to_string, separator))
		goto actions_to_string_fail;
	iter_free(it);
	return strbuilder_consume(sb);
	
actions_to_string_fail:
	free(sb); iter_free(it);
	return NULL;
}


static char* macro_to_string(Action* a) {
	Macro* x = container_of(a, Macro, action);
	return actions_to_string(x->children, "; ");
}

static void macro_dealloc(Action* a) {
	Macro* x = container_of(a, Macro, action);
	MULTICHILD_DEALLOC(x);
	free(x);
}

void compress_actions(ActionList lst) {
	for(size_t i=0; i<list_len(lst); i++) {
		Action* a = list_get(lst, i);
		scc_action_compress(&a);
		list_set(lst, i, a);
	}
}

static Action* compress(Action* a) {
	Macro* x = container_of(a, Macro, action);
	compress_actions(x->children);
	return a;
}


static inline void next(Macro* x) {
	x->active ++;
	if (x->active >= list_len(x->children)) {
		// Executed all children. What a day...
		x->active = (x->repeat) ? 0 : -1;
	}
}

static inline bool finished(Macro *x) {
	return x->active == -1;
}

static void timer(Mapper* m, void* userdata) {
	Macro* x = (Macro*)userdata;
	Action* c = list_get(x->children, x->active);
	// Macro works through this timer. Every time it's called, 'button' is either
	// pressed or released on one of child actions.
	if (x->press) {
		c->button_press(c, m);
		x->press = false;
	} else {
		c->button_release(c, m);
		x->press = true;
		// Sucesfully executed 'press' and 'release'. Execute next child in order.
		next(x);
	}
	
	if (!finished(x)) {
		// Still have children to execute.
		// Three are hiding in bush nearby, but it's not like any of those can control golems.
		uint32_t hold_time = 0;
		c = list_get(x->children, x->active);
		while (c->type == KW_SLEEP) {
			next(x);
			if (finished(x)) {
				// All remaining actions are just sleeps, if we are not in 'repeat',
				// it's safe to end here.
				return;
			}
			hold_time += sor_get_sleep_time(c);
			c = list_get(x->children, x->active);
		}
		if (hold_time < 0) hold_time = 1;
		m->schedule(m, hold_time, &timer, x);
	}
}

static void button_press(Action* a, Mapper* m) {
	// Macro can be executed only by pressing button
	Macro* x = container_of(a, Macro, action);
	if (list_len(x->children) < 1)
		return;		// Empty macro
	if (x->active >= 0)
		return;		// Already executing this macro
	x->active = 0;
	x->press = true;
	timer(m, x);
}


static void set_sensitivity(Action* a, float x, float y, float z) {
	Macro* ma = container_of(a, Macro, action);
	FOR_ALL_CHILDREN(c->extended.set_sensitivity, extended.set_sensitivity, x, y, z);
}

static void set_haptic(Action* a, HapticData hdata) {
	Macro* ma = container_of(a, Macro, action);
	FOR_ALL_CHILDREN(c->extended.set_haptic, extended.set_haptic, hdata);
}

void macro_set_repeat(Action* a, bool repeat) {
	ASSERT(a->type == KW_MACRO);
	Macro* x = container_of(a, Macro, action);
	x->repeat = repeat;
}

bool macro_add_from_params(Action* a, ParameterList lst) {
	ASSERT(a->type == KW_MACRO);
	Macro* x = container_of(a, Macro, action);
	if (!list_allocate(x->children, list_len(lst)))
		return false;		// OOM
	
	FOREACH_IN(Parameter*, param, lst) {
		Action* a = scc_parameter_as_action(param);
		list_add(x->children, a);
		RC_ADD(a);
	}
	
	return true;
}


static ActionList get_children(Action* a) {
	Macro* x = container_of(a, Macro, action);
	return scc_copy_action_list(x->children);
}

static ActionList get_children_ref(Action* a) {
	Macro* x = container_of(a, Macro, action);
	return x->children;
}


Action* scc_macro_new(Action** actions, size_t action_count) {
	ActionList lst = list_new(Action, action_count);
	Macro* x = malloc(sizeof(Macro));
	if ((x == NULL) || (lst == NULL)) {
		free(x);
		list_free(lst);
		return NULL;
	}
	
	scc_action_init(&x->action, KW_MACRO, AF_ACTION, &macro_dealloc, &macro_to_string);
	x->action.compress = &compress;
	x->action.button_press = &button_press;
	x->action.extended.set_sensitivity = &set_sensitivity;
	x->action.extended.get_children = &get_children;
	x->action.extended.set_haptic = &set_haptic;
	
	x->active = -1;
	x->repeat = false;
	x->children = lst;
	for (size_t i=0; i<action_count; i++) {
		list_add(lst, actions[i]);
		RC_ADD(actions[i]);
	}
	
	return &x->action;
}

bool scc_macro_add_action(Action* m, Action* a) {
	if (0 != strcmp(m->type, KW_MACRO)) {
		// 'm' is not a macro
		WARN("scc_macro_add_action: First parameter has to be a macro");
		return false;
	}
	if (0 == strcmp(a->type, KW_MACRO)) {
		// 'a' is a macro
		WARN("scc_macro_add_action: 2nd parameter can not be a macro");
		return false;
	}
	Macro* x = container_of(m, Macro, action);
	if (!list_add(x->children, a))
		return false;
	RC_ADD(a);
	return true;
}


/** Common code for scc_macro_combine and scc_multiaction_combine */
Action* combine(const char* keyword, Action* a1, Action* a2, ActionList (*get_children)(Action*), Action* (*constructor)(Action**, size_t)) {
	Action* x = NULL;
	if (0 == strcmp(a1->type, keyword)) {
		// If a1 is macro, I'll take all actions from it instead of adding
		// macro itself.
		ActionList children = get_children_ref(a1);
		x = constructor(children->items, list_len(children));
	} else {
		x = constructor(&a1, 1);
	}
	if (x == NULL)
		return NULL;		// return NULL
	
	if (0 == strcmp(a2->type, keyword)) {
		// If a2 is macro, I'll copy actions from it to Macro created with a1
		ActionList children1 = get_children_ref(x);
		ActionList children2 = get_children_ref(a2);
		if (!list_add_all(children1, children2))
			goto combine_fail;					// Failed to allocate space for items from 2nd
		// For 1st set of items, constructor adds new references. For this one,
		// list_add_all does not, so they are added here.
		list_foreach(children2, &ref_action);
	} else {
		ActionList children = get_children_ref(x);
		if (!list_allocate(children, 1))
			goto combine_fail;					// Failed to allocate space for single item :(
		list_add(children, a2);
		RC_ADD(a2);
	}
	
	return x;
	
combine_fail:
	RC_REL(x);
	return NULL;
}

Action* scc_macro_combine(Action* a1, Action* a2) {
	return combine(KW_MACRO, a1, a2, &get_children_ref, &scc_macro_new);
}

