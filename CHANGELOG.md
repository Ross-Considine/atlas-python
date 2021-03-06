# *CHANGELOG* for the *Atlas* toolkit

- Common to **all** bindings,
- does **not** concern the native code,

## 2019-05-09

- *Node.js*:
	- changing some stuff related to *Repl.it*,
	- switching to 0.9.2,

## 2019-05-07

- *Python*:
  - `setLayoutXSL(…)` can now take a string containing the XSL data,
  - switching to 0.9.6,

## 2019-05-02

- *Python*:
  - modification of the *Repl.it* related stuff,
  - `CreateHTML(…)` becomes an alias of `CreateXML(…)`,
  - switching to 0.9.5

## 2019-04-30

- *Node.js*:
  - adding some features related to *Repl.it*,
  - switching to 0.9.1
- *Python*:
  - adding some features related to *Repl.it*,
  - switching to 0.9.4

## 2019-04-24

- *Python*:
  - modifications to fit with *Pypi*,
  - switching to 0.9.1,

## 2019-04-18

- switching to 0.9.0 due to a *RunKit* issue,

## 2019-04-17

- *Node.js*, *Python*:
  - switching to 0.8.0

## 2019-04-16

- *Node.js*, *Python*:
  - `setLayout(...)` accepts now an *XML* (from the *Atlas* toolkit) object in addition to *HTML* string.

## 2019-04-03

- *Ruby*:
  - fixing issues occurring under *POSIX*,
  - switching to version 0.7.1,

## 2019-03-04

- one back-end now only opens one (multiplexed) connection to the proxy, instead of one per session,
- switching to version 0.7,

## 2018-12-22

- the opening of the web browser does no more block the entire app under some *Linux* distribution,

## 2018-12-18

- handling error on token,

## 2018-12-14

- switching to version 0.6,

## 2018-12-11

- removing the new session related stuff,

## 2018-12-07

- *Python*
  - fixing `(set|remove)Attribute(…)` bug,
- **ALL**:
  - switching to new protocol and resetting version,
  - switching to version 5.2,

## 2018-11-24

- *Node.js*:
  - fixing error message displayed when not able to connect,

## 2018-11-23

- *Node.js* and *Python* bindings:
  - fixing error in handling environment variables for proxy/web address/port,
  - switching to version 0.5.1a,

## 2018-11-22

- both application (web) address/port and proxy address/port can now be set with environment variables,
- switching to version 0.5.1,

## 2018-11-20

- switching to protocol version 1,

## 2018-11-18
- *Node.js* binding
  - version 0.5.0b; only to fix a *NPM*/*Github* issue,

## 2018-11-17

- *Node.js* binding:
  - the *URL* is now also automatically opened in a web browser with *Termux* (*Android*),
  - version 0.5.0a

## 2018-11-15

- introducing the *Python* binding,

## 2018-11-09

- version 0.5.0,

## …

## 2018-09-03

- version 0.2.0,

## 2018-08-19

- version  0.1.9,

## 2018-04-20

- *atlas-java*
  - simplification,
- all bindings:
  - version  0.1.0,

## 2018-03-07

- _UnJSq_ becomes _Atlas_ (toolkit),

## 2018-02-03

- adding `execute`, `focus`, `removeAttribute`,

## 2018-01-10

- *unjsq-node*:
    - fixing compilation issues under *macOS*.