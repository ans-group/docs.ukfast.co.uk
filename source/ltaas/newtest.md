# Create A Test

Creating a test is relatively easy, deciding what to test is less so. For deciding
what to test, see // TODO //.

## Test Details

First head over to the "Create a Test" page. You can get there from the domains page,
or alternatively from the tests page. You should be greated with the following section
first.

![Create test details section](files/create-details.png)

```eval_rst
.. note::

   If you clicked "Create a new test" from the domain screen, you'll have the domain
   auto-selected and won't be able to change it.

```

The first step is to fill in the `Test Name`. This will be visible in the test table,
so be descriptive if you plan on running tests regularly so you know what has run
and when.

Next select the `protocol`. If you're not sure what the protocol is, in your browser
navigate to the website. You may be redirected to the secure (https) version of your
site. If that's the case, you should select https, otherwise the redirects will
cause your test to fail. If you site has a certificate installed you should always
select https. If you don't have a certificate installed, select http.

The next field is `Domain`. Drop down from the list. If you have a few domains here,
select the one you wish to test. If you have just the one, your selection is much
easier.

The last field on the details form is the `path`. Putting the path as / will mean
the traffic will likely be hitting your homepage. If you have an alternative homepage
and wished to test that, you could enter /home, if /home was your homepage. A good
rule of thumb to use is to enter whatever is in your browsers url bar (minus the
protocol and domain).  

## Test Settings

// TODO //

## Schedule

The schedule section lets you either run the test now, later at a specified time and
date, or on a repeating schedule.

If you want to quickly run a test, just select the `Run now` option and then click
the Run now button. You should be sent to the test screen where you will see your
test available.

If you'd like to run a test at a different time, for example out of business hours,
then you have the option to do that. Tick the `Schedule` option and fill in the two
fields. It will ask for a date and a time.

```eval_rst
.. note::

   The schedule system will likely not execute at the exact time entered, but will
   execute at a time very close to it. This is to ensure resources aren't execessive
   at common time schedules.

```

Lastly, both Run Now and Schedule offer the ability to `Repeat` the test. This is a
good feature if you regularly develop your site and want more confidence in your
solutions ability to cope with the traffic levels you expect, both at a software
and hardware level. All you need to do is tick the Repeat option and enter a
quantity and a frequency. For example, entering a quantity of 7 and a Frequency of
Days, would mean the test runs every 7 days. You could achieve the same by entering
a quantity of 1 and a Frequency of weeks.
