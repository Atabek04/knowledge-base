---
aliases: [Spring Factory Method, BeanFactory pattern, FactoryBean pattern, Spring FactoryBean]
---

Spring is built around the [[The Factory Method pattern lets subclasses decide which object to instantiate by overriding a factory method|Factory Method pattern]] at multiple layers. The common thread: a client requests an object by name or type and never calls `new` — the factory decides what to build and how.

---

### BeanFactory — the root factory interface

<mark style="background: #FFF3A3A6;">**`BeanFactory`**</mark> is the core factory interface. Its `getBean()` overloads are the factory methods: the caller passes a name or type, the container returns either a cached singleton or a fresh prototype. Instantiation strategy is fully encapsulated.

```java
UserService svc = beanFactory.getBean("userService", UserService.class);
```

The Spring Javadoc explicitly references both the **Prototype** and **Singleton** design patterns as variants the same factory method supports — the caller never changes its code to switch between them.

**Concrete implementations** (each a ConcreteCreator in GoF terms):

- `DefaultListableBeanFactory` — the standard full-featured container
- `XmlBeanFactory` (legacy) — bean definitions from XML
- `ApplicationContext` and all its variants — extended factory with auto-wiring and event propagation

---

### FactoryBean — factory method as an extension point

<mark style="background: #FFF3A3A6;">**`FactoryBean<T>`**</mark> is Spring's named extension point for the pattern. Implement it when a bean's creation requires logic too complex for a plain constructor.

```java
public interface FactoryBean<T> {
    @Nullable T getObject() throws Exception;  // the factory method
    @Nullable Class<?> getObjectType();
    default boolean isSingleton() { return true; }
}
```

`getObject()` is the factory method. Any bean in the container that implements `FactoryBean` is treated specially: Spring calls `getObject()` and injects the *result*, not the factory itself.

To retrieve the `FactoryBean` instance directly, prefix the bean name with `&`:

```java
FactoryBean<?> fb = (FactoryBean<?>) ctx.getBean("&myFactoryBean");
```

#### Why this maps cleanly to GoF

| GoF role | Spring class |
|---|---|
| Abstract Creator (interface) | `FactoryBean<T>` |
| factory method | `getObject()` |
| Concrete Creator | `ProxyFactoryBean`, `LocalSessionFactoryBean`, etc. |
| Product | the object `getObject()` returns |

---

### ApplicationContext — extended factory with @Bean methods

`ApplicationContext` extends `BeanFactory`. On top of `getBean()`, it adds a second factory-method mechanism: <mark style="background: #FFF3A3A6;">**`@Bean` methods inside `@Configuration` classes**</mark>.

Each `@Bean` method is a Java factory method — Spring calls it at startup to produce and register the bean. The method name becomes the bean name; the return type becomes its type.

```java
@Configuration
public class DataSourceConfig {

    @Bean  // Spring calls this to produce the DataSource bean
    public DataSource dataSource() {
        HikariDataSource ds = new HikariDataSource();
        ds.setJdbcUrl("jdbc:postgresql://localhost/mydb");
        return ds;
    }
}
```

`ApplicationContext` also loads all singleton beans eagerly and auto-registers `BeanPostProcessor` instances, which decorate created objects before injection — a post-creation hook `BeanFactory` lacks without manual setup.

---

### Built-in FactoryBean implementations

Spring ships several ConcreteCreators out of the box. Each hides a heavyweight creation process behind `getObject()`.

#### ProxyFactoryBean

<mark style="background: #ABF7F7A6;">Creates an AOP proxy</mark> (JDK dynamic or CGLIB) wrapping a target bean with interceptors. The factory decides which proxy strategy to use; the caller just gets a proxied object.

```xml
<bean id="myServiceProxy" class="org.springframework.aop.framework.ProxyFactoryBean">
    <property name="targetName" value="myService"/>
    <property name="interceptorNames"><list><value>loggingInterceptor</value></list></property>
    <property name="proxyInterfaces" value="com.example.MyService"/>
</bean>
```

#### LocalSessionFactoryBean

<mark style="background: #ABF7F7A6;">Creates a Hibernate `SessionFactory`</mark> — a heavyweight object requiring dialect configuration, entity scanning, and datasource wiring. All bootstrap complexity is hidden behind `getObject()`.

#### JndiObjectFactoryBean

<mark style="background: #ABF7F7A6;">Performs a JNDI lookup</mark> at startup and exposes the result (a `DataSource`, `Queue`, or `ConnectionFactory`) as a Spring-managed singleton. Swapping it for `DriverManagerDataSource` requires no change to any consumer.

#### TransactionProxyFactoryBean

<mark style="background: #ABF7F7A6;">Creates a transactional AOP proxy</mark> around a target. Superseded by `@Transactional`, but illustrates the pattern directly.

---

### The pattern's benefit in Spring

<mark style="background: #FF000040;">Without `FactoryBean`</mark>, any bean that requires non-trivial creation (proxying, JNDI lookup, Hibernate bootstrap) would need to be wired manually — exposing all intermediate objects to the container and to callers. `FactoryBean` keeps the factory in the container graph without leaking its internals.

The contract is: the container registers the factory; consumers receive the product. The factory method (`getObject()`) is the seam that makes substitution possible — swap `JndiObjectFactoryBean` for `DriverManagerDataSource` by changing one bean definition, zero consumer changes.

---

### Read more
- [[The Factory Method pattern lets subclasses decide which object to instantiate by overriding a factory method]]
- [[Factory Method in Java uses an abstract creator class whose subclasses override the factory method]]
- [[Design Patterns - MOC]]
- [[Spring Ecosystem - MOC]]
